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

alias src="python3 ~/.../Gitignore/src/main.py"
src --list/-l
src --list/-l | grep py
src --update
src python pycharm+all
```

## API

- list
  - `https://www.toptal.com/developers/gitignore/api/list?format=lines`

- get
  - `https://www.toptal.com/developers/gitignore/api/python,pycharm+all`
