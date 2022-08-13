# src/main.py
from api import API


def main():
    # get user input
    lists = API.get_list()
    print("\n".join(lists))


if __name__ == "__main__":
    main()
