# setup.py
from setuptools import find_packages, setup


def load_requirements() -> list:
    with open("./requirements.txt", "r") as req:
        return req.read().splitlines()


setup(
    name="gitignore-list",
    version="0.3.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ig=src.main:main",
        ],
    },
    install_requires=load_requirements(),
)
