import json
import requests


def load():
    with open('data.json', 'r') as files:
        data = json.load(files)
        for detail in data['channel']['item']:
            if detail['content_encoded'] is not None and detail['content_encoded'] is not ' ':
                data_mapper = mapper(detail)
                print(data_mapper)
                print("0000000000000000000000000000000000000000000000000000")
                post_data(data_mapper)
                print("0000000000000000000000000000000000000000000000000000")


def mapper(param):
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
            "wp_post_modified": param['wp_post_modified'],
            "wp_post_modified_gmt": param['wp_post_modified_gmt'],
            "wp_comment_status": param['wp_comment_status'],
            "wp_ping_status": param['wp_ping_status'],
            "wp_post_name": param['wp_post_name'],
            "wp_status": param['wp_status'],
            "wp_post_parent": param['wp_post_parent'],
            "wp_menu_order": param['wp_menu_order'],
            "wp_post_type": param['wp_post_type'],
            "wp_post_password": param['wp_post_password'],
            "wp_is_sticky": param['wp_is_sticky'],
            "category": "domain"
        }
    }
    return model

def post_data(data):
    response = requests.post('http://localhost:1337/api/migrates', json=data)
    print(response.json())


if __name__ == "__main__":
    load()