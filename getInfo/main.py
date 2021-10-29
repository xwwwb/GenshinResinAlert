import json
from typing import Literal, Any

import requests

from .headers import headers
from .utils import get_server

session = requests.session()


def request(url: str, cookie: str, method: Literal['GET', 'POST'] = 'GET', **kwargs: Any):
    query: dict = kwargs.get('params', {})
    body = kwargs.get('data', '')
    response = session.request(method, url, headers=headers.new(
        cookie, query, body), **kwargs)
    return response


def main() -> None:
    path = "./config.json"
    with open(path, 'r+') as f:
        json_data = json.load(f)

    uid = str(json_data['uid'])
    cookie = json_data['cookie']
    server: str = get_server(uid)
    body: dict = {
        'server': server,
        'role_id': uid
    }

    url = 'https://api-takumi.mihoyo.com/game_record/app/genshin/api/dailyNote'
    data = request(url, params=body, cookie=cookie).text
    data = json.loads(data)
    resin = data.get('data').get('current_resin')
    return f"现有{resin}个树脂"
