import requests
import time
import re

token = 'c6b3e957c6b3e957c6b3e9578dc6dd1062cc6b3c6b3e95798a7bb0603b5aabb2c8bdf09'
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


