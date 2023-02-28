from menu import main_menu, ops
from menu.menu_ops import screen_transition


def main():
    while True:
        screen_transition()
        main_menu()
        choice = input('\n[?]: ')
        ops(choice)


if __name__ == '__main__':
    main()



