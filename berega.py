import requests
import time
import re

token = 'c38aa09bc38aa09bc38aa09b74c3e44553cc38ac38aa09b9d84b30e048f8ec39a7eaba6'
version = 5.103
domain = 'beregaonline_tutaev'
count = 100
offset = 0

response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'count': 1,
                            'offset': offset
                        })

post_count = response.json()['response']['count']

while offset < post_count:
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': count,
                                'offset': offset
                            })
    offset += 100
    data = response.json()['response']['items']
    for i in data:
        string = i['text']
        matched_string = re.search('#администрацияТМР', string)
        if matched_string != None:
            print(string)
    time.sleep(0.5)


