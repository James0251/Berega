import requests

token = 'c38aa09bc38aa09bc38aa09b74c3e44553cc38ac38aa09b9d84b30e048f8ec39a7eaba6'
version = 5.103
domain = 'beregaonline_tutaev'

response = requests.get('https://api.vk.com/method/wall.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'domain': domain,
                            'count': 100
                        })

data = response.json()['response']['items']
print(1)