import json
import requests

url = 'https://media.digitalarkivet.no/api/v1/db/browse?tags%5B%5D=373'
headers = {'auth-token': '9189f9c0-e5cd-4fcf-b8fd-ae864c284ec1', 'content-type': 'application/json'}
response = requests.get(url,  headers=headers)

for entry in response:
    print('\n',entry)