# src/api.py
import requests


class API:
    LIST_URL = "https://www.toptal.com/developers/gitignore/api/list?format=lines"
    API_URL = "https://www.toptal.com/developers/gitignore/api/{}"

    @classmethod
    def get_list(cls) -> list:
        """
        get each language .gitignore lists

        :return: language_names list via gitignore.is api
        """
        response = requests.get(cls.LIST_URL)

        if response.status_code != 200:
            raise requests.RequestException(f"Can't get response from '{cls.LIST_URL}'")

        return response.text.split("\n")

    @classmethod
    def get_gitignore(cls, language_names: list) -> str:
        """
        get a gitignore via gitignore.io api
        URL: https://www.toptal.com/developers/gitignore/api/python,pycharm+all

        :param language_names: list like ["ocaml", "python", "perl", "ruby"]
        :return:
        """
        response = requests.get(cls.API_URL.format(",".join(language_names)))

        if response.status_code != 200:
            raise requests.RequestException(f"Can't get response from '{cls.API_URL}'")

        return response.text.strip()
