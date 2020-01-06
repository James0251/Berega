import requests
import time
import re

token = '456058734560587345605873f8450ebdbb44560456058731b7305a82c940e0aa7b825bf'
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


