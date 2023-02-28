from sys import exit
from os import system
from time import sleep
from api import (
    send_request,
    delete_manifest,
    CATALOG,
    USER,
    PASS
)

def list_repositories():
    response = send_request(CATALOG)
    repos = dict()
    if response:
        if response.status_code == 200:
            for index, repo in enumerate(response.json()['repositories']):
                repos[index + 1] = repo
            return repos, response.url
        else:
            print(f'API call failed with status code: {response.status_code}')
    else:
        print(f'API call returned an empty response: {response}')


def get_tags(repo_name, ret_val=False):
    url = f'https://docker.mysck.net/v2/{repo_name}/tags/list'
    response = send_request(url)
    tags = dict()

    if response:
        if response.status_code == 200:
            print(f'\n\tTags for {repo_name}\n')
            tag_list = response.json()['tags']

            if tag_list:
                for index, tag in enumerate(tag_list):
                    tag_index = index + 1
                    print(f'{tag_index}) {tag}')
                    tags[tag_index] = tag
            else:
                print(f'No images found for {repo_name}')

            if ret_val:
                return tags

def get_digest(url):
    response = send_request(url)
    if response:
        if response.status_code == 200:
            digest = response.headers['docker-content-digest']
            print(f'Got digest: {digest}')

            return digest
        else:
            print(f'API request failed with status code {response.status_code}')
    else:
        print(f'API request returned empty response')


def delete_tag(tag, repo):
    manifest_url = f'https://docker.mysck.net/v2/{repo}/manifests/{tag}'
    print(f'Deleting {tag}\n')

    digest = get_digest(manifest_url)
    delete_url = f'https://docker.mysck.net/v2/{repo}/manifests/{digest}'

    response = delete_manifest(delete_url)

    if response:
        if response.status_code == 200 or response.status_code == 202:
            print('Image successfully deleted.')
        else:
            print(f'API request failed with status code {response.status_code}')
    else:
        print(f'API request returned empty response')

    screen_pause()
    return response.status_code


def screen_pause():
    user_input = input('\n[!] Press ENTER to continue...')
    del user_input

def screen_transition():
    system('clear')
    sleep(1)

def exit_app():
    exit(0)








