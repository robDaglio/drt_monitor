#!/usr/bin/env python
import requests
import os
import sys
from requests.auth import HTTPBasicAuth
from time import sleep

USER = 'kbadmin'
PASS = 'Sck2Support'
ALL_REPOS = 'https://docker.mysck.net/v2/_catalog'


def select_op(choice):
    if choice == '1':
        show_repos(get_repos())
    if choice == '2':
        show_tags(get_tags())
    if choice == '3':
        delete_image()
    if choice == '4':
        print('\nExiting...')
        sleep(2)
        exit()


def get_manifests(image_tag):
    url = f"https://docker.mysck.net/v2/automation/pos_api_depleter/manifests/{image_tag}"
    headers = {
        'Accept': 'application/vnd.docker.distribution.manifest.v2+json'
    }

    try:
        response = requests.head(url, headers=headers, auth=HTTPBasicAuth(USER, PASS))
        return response
    except (
            requests.ConnectionError,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            Exception
    ) as e:
        print(f'Failed to retrive manifest: {e}')
        exit()


def send_delete(payload):
    try:
        response = requests.delete(payload, auth=HTTPBasicAuth(USER, PASS))
        return response
    except (
            requests.ConnectionError,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.Timeout,
            requests.exceptions.TooManyRedirects,
            Exception
    ) as e:
        print(f'Failed to delete specified image: {e}')


def delete_image():
    i_tag = input('[?] Image tag: ')

    try:
        digest = dict(get_manifests(i_tag).headers)['Docker-Content-Digest']
        delete_image = f'https://docker.mysck.net/v2/{i_tag}/manifests/{digest}'
        response = send_delete(delete_image)
        if response:
            if response.status_code == 200:
                print(f'Image {i_tag} deleted successfully...')
            else:
                print(f'Delete failed | response code: {response.status_code}')
        else:
            print(response)
    except (KeyError, IndexError) as e:
        print(f'Digest not found for {i_tag}')
        exit()


def send_request(url):
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USER, PASS))
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


def show_repos(response):
    os.system('clear')
    sleep(1)

    if response:
        if response.status_code == 200:
            print(f'\n\tDocker repositories for {response.url}\n')
            for index, repo in enumerate(response.json()['repositories']):
                print(f'{index + 1}) {repo}')


def get_repos():
    return send_request(ALL_REPOS)


def get_repo_name():
    repo_name = input('[?] Repo name: ')
    return repo_name


def get_tags():
    os.system('clear')
    repo = get_repo_name()
    url = f'https://docker.mysck.net/v2/{repo}/tags/list'
    return (send_request(url), repo)


def show_tags(repo_info):
    os.system('clear')
    sleep(1)

    if repo_info[0]:
        if repo_info[0].status_code == 200:
            print(f'\n\tTags for {repo_info[1]}\n')
            for index, repo in enumerate(repo_info[0].json()['tags']):
                print(f'{index + 1}) {repo}')
        else:
            print('No tags found...')
    else:
        print('Repository not found...')


def verify_input(user_choice):
    if user_choice not in ['1', '2', '3', '4']:
        print('Invalid input')
        return False
    else:
        return True


def main_menu():
    while True:
        os.system('clear')
        sleep(1)
        print('\n\tDocker Registry API Interface\n')
        for menu_item in [
            '1) List all repositories',
            '2) Search tags by repo name',
            '3) Delete image by tag',
            '4) Exit'
        ]:
            print(f'{menu_item}')

        choice = input('\n[?]: ')
        if verify_input(choice):
            select_op(choice)
            sys.stdin.flush()
        else:
            pass

        input('\nPress any key to continue...')


if __name__ == '__main__':
    main_menu()
