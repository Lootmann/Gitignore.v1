# src/main.py
import argparse

from api import API
from cli import CLI


def main():
    parser = argparse.ArgumentParser(description="Get .gitignore from gitignore.io")

    parser.add_argument("--list", action="store_true")
    parser.add_argument("-l", action="store_true")
    parser.add_argument("languages", nargs="*")

    args = parser.parse_args()

    if args.list or args.l:
        CLI.print_list(API.get_list())
        return

    if len(args.languages) > 0:
        CLI.print(API.get_gitignore(args.languages))
        return

    parser.print_usage()


if __name__ == "__main__":
    main()
