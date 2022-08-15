# src/main.py
import argparse

from api import API
from cache import Cache
from cli import CLI


def main():
    parser = argparse.ArgumentParser(description="Get .gitignore from gitignore.io")

    parser.add_argument("--list", action="store_true", help="show args that can allow language names")
    parser.add_argument("-l", action="store_true", help="same on above")
    parser.add_argument("--update", action="store_true", help="update gitignore list cache")
    parser.add_argument("languages", nargs="*")

    args = parser.parse_args()

    if args.list or args.l:
        CLI.print_list(API.get_gitignore_list())
        return

    if args.update:
        Cache.update_gitignore_list(API.get_gitignore_list_from_api())
        CLI.print("success to update gitignore-list")
        return

    if len(args.languages) > 0:
        CLI.print(API.get_gitignore(args.languages))
        return

    parser.print_usage()


if __name__ == "__main__":
    main()
