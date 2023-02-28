from enum import Enum
from .menu_ops import *

class Menu(Enum):
    MAIN_MENU = {
        '1': ') List all repositories',
        '2': ') Search tags by repo name',
        '3': ') Delete image by tag',
        '4': ') Exit'
    }

def main_menu():
    print('\n\tDocker Registry API Interface\n')
    for index, menu_item in Menu.MAIN_MENU.value.items():
        print(f'{index}{menu_item}')


def repo_sub_menu(repos, url):
    screen_transition()
    back = len(repos) + 1

    while True:
        screen_transition()

        print(f'\n\tDocker repositories for {url}\n')
        for index, repo in repos.items():
            print(f'{index}) {repo}')
        print(f'\n{back}) Go back.')
        print('00) Exit.')

        print('\nSelect a repository to view all tag(s).')
        choice = input('[?]: ')

        if (choice == '' or choice.isalpha()) or \
        (int(choice) not in repos.keys() and choice != str(back)) \
        and choice != '00':
            print('[x] Invalid input.')
        else:
            if choice == str(back):
                break
            elif choice == '00':
                exit_app()
            else:
                screen_transition()
                search_by_repo_name(repo_name=repos[int(choice)])
                screen_pause()


def search_by_repo_name(repo_name=None):
    if repo_name:
        get_tags(repo_name)
    else:
        repos, url = list_repositories()
        while True:
            print("\nEnter 'back' to return to main menu.")
            repo_name = input('[?] Repo name: ').lower()

            if repo_name not in repos.values() and repo_name != 'back':
                print('[x] Repository not found.')
            else:
                if repo_name == 'back':
                    break
                else:
                    get_tags(repo_name)


def delete_image_by_tag():
    repos, url = list_repositories()
    back = len(repos) + 1

    while True:
        screen_transition()

        print(f'\n\tDocker repositories for {url}\n')
        for index, repo in repos.items():
            print(f'{index}) {repo}')
        print(f'\n{back}) Go back.')
        print('00) Exit.')

        print('\nSelect a repository to view all tag(s).')
        choice = input('[?]: ')

        if (choice == '' or choice.isalpha()) or \
        (int(choice) not in repos.keys() and choice != str(back)) \
        and choice != '00':
            print('[x] Invalid input.')
        else:
            if choice == str(back):
                break
            elif choice == '00':
                exit_app()
            else:
                tags = get_tags(str(repos[int(choice)]), ret_val=True)
                list_delete(tags, repos[int(choice)])


def list_delete(tags, repo):
    back = len(tags) + 1

    while True:
        screen_transition()
        print(f'\n\tTags for {repo}\n')

        for index, tag in tags.items():
            print(f'{index}) {tag}')
        print(f'\n{back}) Go back.')

        print('\nSelect a tag to delete.')
        choice = input('[?]: ')

        if (choice == '' or choice.isalpha()) or \
        (int(choice) not in tags.keys() and choice != str(back)):
            print('[x] Invalid input.')
        else:
            if choice == str(back):
                break
            else:
                status = delete_tag(tags[int(choice)], repo)
                if status == 200 or status == 202:
                    break


def ops(choice):
    if choice not in Menu.MAIN_MENU.value.keys():
        print('[x] Invalid input.')
    else:
        if choice == '1':
            repos, url = list_repositories()
            repo_sub_menu(repos, url)
        elif choice == '2':
            search_by_repo_name()
        elif choice == '3':
            delete_image_by_tag()
        elif choice == '4':
            exit_app()


