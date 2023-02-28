import requests
from requests.auth import HTTPBasicAuth

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
        response = requests.delete(url, headers=HEADERS, auth=HTTPBasicAuth(USER, PASS))
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