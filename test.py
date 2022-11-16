import xml.etree.ElementTree as ET
import json

# configuration: change filename and namespace if needed
xml_name = '/home/nasri/Workspace/GGWP/strapi-research/ggwpid.fitri.xml'
out_name = r'ggwpid.fitri.json'

ns = {
    'wp': 'http://wordpress.org/export/1.2/',
    'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'wfw': 'http://wellformedweb.org/CommentAPI/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

# prepare ns map to replace tag name
ns_map = {}
for n in ns:
    pattern = '{' + ns[n] + '}'
    ns_map[pattern] = n + '_'

# parse xml
tree = ET.parse(xml_name)
root = tree.getroot()

# get channel
channel = root.find('channel')

# site data
site = {}


def format_ns(tag):
    """
    format tag with namespace url to simplified tag
    :param tag: 
    :return: 
    """
    global ns_map
    for p in ns_map:
        if p in tag:
            return tag.replace(p, ns_map[p])
    return tag


def add_data(key, value, data):
    """
    add new key value to data, create/append to list if needed
    :param key: 
    :param value: 
    :param data: 
    :return: 
    """
    list_type_keys = [
        'wp_author',
        'item',
        'category',
        'wp_postmeta',
        'wp_comment',
        'wp_commentmeta'
    ]
    if key in list_type_keys:
        if key not in data:
            data[key] = []
        data[key].append(value)
    else:
        data[key] = value


def iterate(element, data):
    """
    iterate through the tree and add elements to site data
    :param element: 
    :param data: 
    :return: 
    """
    children = list(element)
    attrs = element.items()
    tag = format_ns(element.tag)
    if len(children) == 0 and len(attrs) == 0:
        # simple tag, add text to data with its tag as key
        add_data(tag, element.text, data)
    else:
        sub_data = {}
        if len(attrs) != 0:
            for a in attrs:
                add_data(a[0], a[1], sub_data)
            add_data('value', element.text, sub_data)
        if len(children) != 0:
            for c in children:
                iterate(c, sub_data)
        add_data(tag, sub_data, data)


# iterate through channel to get site data
iterate(channel, site)

# write json to file
f = open(out_name, 'w')
f.write(json.dumps(site))
f.close()