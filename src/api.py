# src/api.py
import requests


class API:
    API_URL = "https://www.toptal.com/developers/gitignore/api/list?format=lines"

    @classmethod
    def get_list(cls) -> list:
        """

        :return: language_names list via gitignore.is api
        """
        response = requests.get(cls.API_URL)

        if response.status_code != 200:
            raise requests.RequestException(f"Can't get response from '{cls.API_URL}'")

        return response.text.split("\n")

    @classmethod
    def get_gitignore(cls, language_names: list) -> str:
        """
        get_gitignore via gitignore.io api
        :param language_names:
        :return:
        """
        return ""
