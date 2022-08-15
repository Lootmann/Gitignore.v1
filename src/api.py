# src/api.py
import sys

import requests

from cache import Cache


class API:
    LIST_URL = "https://www.toptal.com/developers/gitignore/api/list?format=lines"
    API_URL = "https://www.toptal.com/developers/gitignore/api/{}"

    @classmethod
    def get_gitignore_list_from_api(cls) -> list:
        """
        get each language ignore list

        :return: ignore list like ["c", "cpp", "d", "elixir", ...]
        """
        response = requests.get(cls.LIST_URL)

        if response.status_code != 200:
            raise requests.RequestException(f"Can't get response from '{cls.LIST_URL}'")

        return response.text.split("\n")

    @classmethod
    def get_gitignore_list(cls) -> list:
        """
        get each language .gitignore lists
        if .gitignore list are cached, return this cache file(ordinary plain text)
        if not, create cached.

        :return: language_names list via gitignore.is api
        """
        if Cache.exists():
            return Cache.get_ignore_list()

        ignore_list = cls.get_gitignore_list_from_api()
        Cache.create_gitignore_list(ignore_list)
        return ignore_list

    @classmethod
    def get_gitignore(cls, language_names: list) -> str:
        """
        get a gitignore via gitignore.io api
        URL: https://www.toptal.com/developers/gitignore/api/python,pycharm+all

        sometimes language_names are not listed on gitignore-list (probably you have some typos),
        cause error

        :param language_names: list like ["ocaml", "python", "perl", "ruby"]
        :return:
        """
        cls.find_language_name_on_cache(language_names)

        response = requests.get(cls.API_URL.format(",".join(language_names)))

        if response.status_code != 200:
            raise requests.RequestException(f"Can't get response from '{cls.API_URL}'")

        return response.text.strip()

    @classmethod
    def find_language_name_on_cache(cls, language_names: list):
        """
        find language name on cache file
        if language name is not on cache, raise Exception.
        and show most "similar" language name.

        TODO:
            The 'similar' is defined by 'edit distance' using dynamic programming.
            lowest edit distance score means most similar name. (I think)

        :param language_names:
        :return: None
        """
        gitignore_set = set(Cache.get_ignore_list())
        not_found = False
        similar_dict = {name: [] for name in language_names}

        # O(N)
        for name in language_names:
            min_score = 100

            # O(log M)
            if name not in gitignore_set:
                not_found = True
                current_list = []

                # calc score O(M)
                for list_name in gitignore_set:
                    # found substring -> pretty similar
                    if name in list_name:
                        current_list.append((list_name, len(name), 0))
                        min_score = 0
                        continue

                    current_score = abs(len(name) - len(list_name))
                    intersection_score = set(name) ^ set(list_name)
                    current_score += len(intersection_score)

                    # less score, more good word == similar word
                    if min_score >= current_score:
                        min_score = current_score
                        current_list.append((list_name, min_score))

                # add good score language name
                for name_list in current_list:
                    if name_list[1] == min_score:
                        similar_dict[name].append(name_list)

        if not_found:
            print("* you typo ?")
            print("*")
            for k, v in similar_dict.items():
                if len(v) >= 1:
                    print(f"* [{k}]")
                    for line in v:
                        print(f"* {line[0]}")
                    print()

            sys.exit(1)
