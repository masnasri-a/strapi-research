import json
import requests
import traceback

def load():
    with open('ggwp-2.json', 'r') as files:
        data = json.load(files)
        for detail in data['channel']['item']:
            if detail['content_encoded'] is not None and detail['content_encoded'] is not ' ':
                data_mapper = mapper(detail)
                print("0000000000000000000000000000000000000000000000000000")
                post_data(data_mapper)
                print("0000000000000000000000000000000000000000000000000000")


def mapper(param):
    try:
        model = {
            "data": {
                "title": param['title'],
                "pubDate": param['pubDate'] ,
                "dc_creator": param['dc_creator'],
                "description": param['description'],
                "content_encoded": param['content_encoded'],
                "wp_post_id": param['wp_post_id'],
                "wp_post_date": param['wp_post_date'],
                "wp_post_date_gmt": param['wp_post_date_gmt'],
                "wp_post_modified": param['wp_post_modified'] if 'wp_post_modified' in param else '',
                "wp_post_modified_gmt": param['wp_post_modified_gmt']if 'wp_post_modified_gmt' in param else '',
                "wp_comment_status": param['wp_comment_status']if 'wp_comment_status' in param else '',
                "wp_ping_status": param['wp_ping_status']if 'wp_ping_status' in param else '',
                "wp_post_name": param['wp_post_name']if 'wp_post_name' in param else '',
                "wp_status": param['wp_status']if 'wp_status' in param else '',
                "wp_post_parent": param['wp_post_parent']if 'wp_post_parent' in param else '',
                "wp_menu_order": param['wp_menu_order']if 'wp_menu_order' in param else '',
                "wp_post_type": param['wp_post_type']if 'wp_post_type' in param else '',
                "wp_post_password": param['wp_post_password']if 'wp_post_password' in param else '',
                "wp_is_sticky": param['wp_is_sticky']if 'wp_is_sticky' in param else '',
                "category": "domain"
            }
        }
        return model
    except:
        traceback.print_exc()
        exit()

def post_data(data):
    response = requests.post('http://localhost:1337/api/migrates', json=data)
    # print(response.json())


if __name__ == "__main__":
    load()