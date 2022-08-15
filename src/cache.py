# src/cache.py
from pathlib import Path


class Cache:
    CACHE_PATH = Path("~/.cache/gitignore-list").expanduser()

    @classmethod
    def exists(cls) -> bool:
        return cls.CACHE_PATH.exists()

    @classmethod
    def create_gitignore_list(cls, ignore_list: list) -> None:
        cls.CACHE_PATH.write_text("\n".join(ignore_list))

    @classmethod
    def get_ignore_list(cls) -> list:
        return cls.CACHE_PATH.read_text().split("\n")
