import requests
from requests.auth import HTTPBasicAuth
import json

USER = 'kbadmin'
PASS = 'Sck2Support'
CATALOG = 'https://docker.mysck.net/v2/_catalog'
HEADERS = {
        'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
    }

def send_request(url):
    try:
        response = requests.get(url, headers=HEADERS, auth=HTTPBasicAuth(USER, PASS))
        return response
    except (
            requests.ConnectionError,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            Exception
    ) as e:
        print(f'Request failed: {e}')
        return None

def delete_manifest(url):
    try:
        response = requests.get(url, headers=HEADERS, auth=HTTPBasicAuth(USER, PASS))
        return response
    except (
            requests.ConnectionError,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            Exception
    ) as e:
        print(f'Request failed: {e}')
        return None

if __name__ == '__main__':
    image = 'snapshot/qpm/aloha_ncr_pos'
    tag = '1.0.0.7'


    docker_url = f'https://docker.mysck.net/v2/{image}/manifests/{tag}'
    response = send_request(docker_url)

    print(response.headers['docker-content-digest'])

