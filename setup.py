# setup.py
from setuptools import find_packages, setup

setup(
    name="gi",
    version="0.3.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gi=gi.main:main",
        ],
    },
)
