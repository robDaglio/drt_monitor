#!/usr/bin/env python
import requests
import json

from requests.auth import HTTPBasicAuth

USER = 'kbadmin'
PASS = 'Sck2Support'

if __name__ == '__main__':
    url = "https://docker.mysck.net/v2/automation/test_pos_api/manifests/0.1.15"
    headers = {
        'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
    }

    response = requests.head(url, headers=headers, auth=HTTPBasicAuth(USER, PASS))
    #response = requests.get(url)
    
    print(dict(response.headers))
