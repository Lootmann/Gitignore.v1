# src/cache.py
from pathlib import Path


class Cache:
    """
    create cache file

    if the 'gitignore-list' file has been created before the class is executed
    and if the file already exists,
    it outputs the contents of the file without checking its contents.
    """

    CACHE_PATH = Path("~/.cache/gitignore-list").expanduser()

    @classmethod
    def exists(cls) -> bool:
        return cls.CACHE_PATH.exists()

    @classmethod
    def create_gitignore_list(cls, ignore_list: list) -> None:
        cls.CACHE_PATH.write_text("\n".join(ignore_list), encoding="utf-8")

    @classmethod
    def update_gitignore_list(cls, ignore_list: list) -> None:
        cls.create_gitignore_list(ignore_list)

    @classmethod
    def get_ignore_list(cls) -> list:
        return cls.CACHE_PATH.read_text(encoding="utf-8").split("\n")
