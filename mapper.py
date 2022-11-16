import json, re
import requests
import traceback
from auth import upsert, set_author

token ='Bearer d5d6a2cc9dbd142067bc5e152a4dd491e0e4c13d28b6a3e96a893be1dd939234340f495454d4bc2da16cf2e02bf712e3c5749798fe513eab8b1461916c1f85f555e8c16075a8584dc4032c0989b25857fde3b4b8f955578772ec833cfbb51288c81b9f574931e2315501758a06fd1e5ba821e24af09b9a9c53d7616a20e40d1c'


def load():
    with open('ggwpid.fitri.json', 'r') as files:
        data = json.load(files)
        for detail in data['channel']['item']:
            if detail['content_encoded'] is not None and detail['content_encoded'] is not ' ':
                data_mapper, creator = mapper(detail)
                if data_mapper is not None:
                    print("0000000000000000000000000000000000000000000000000000")
                    post_data(data_mapper, creator)
                    print("0000000000000000000000000000000000000000000000000000")


def mapper(param):
    try:
        raw_title = param['title']
        if param['title'] == None:
            return None
        else:
            raw_title = re.sub(r'[!@#$?.,]','',raw_title )
        slug_raw = str(raw_title).split(' ')
        slug = '-'.join(slug_raw[0:4]).lower()
        model = {
            "data": {
                "title": param['title'],
                "pubDate": param['pubDate'] ,
                "dc_creator": param['dc_creator'],
                "description": param['description'],
                "content_encoded": param['content_encoded'],
                "slug":slug
            }
        }
        upsert(param['dc_creator'])
        return model, param['dc_creator']
    except:
        traceback.print_exc()
        exit()

def post_data(data, creator):
    # pass
    response = requests.post('http://103.176.79.228:1337/api/wordpresses', json=data, headers={'Authorization':token})
    if response.status_code == 200:
        set_author(creator)


if __name__ == "__main__":
    load()