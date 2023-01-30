# Gitignore

create `.gitignore` automatically via `https://www.toptal.com/developers/gitignore`

## Requirements

`requests`

## Usage

```shell
python3 src/main.py --list
python3 src/main.py -l
python3 src/main.py --update
python3 src/main.py python pycharm

ig --list/-l
ig --list/-l | grep py
ig --update
ig python pycharm+all > .gitignore
```

## API

- list
  - `https://www.toptal.com/developers/gitignore/api/list?format=lines`

- get
  - `https://www.toptal.com/developers/gitignore/api/python,pycharm+all`
