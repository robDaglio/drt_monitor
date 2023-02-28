#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth

USER = 'kbadmin'
PASS = 'Sck2Support'

image_tag = '1.0.0.3'
url = f"https://docker.mysck.net/v2/automation/pos_api_depleter/manifests/{image_tag}"

headers = {
    'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
}

response = requests.get(url, headers=headers, auth=HTTPBasicAuth(USER, PASS)).json()

for k, v in response.items():
    print(f'{k}: {v}')




