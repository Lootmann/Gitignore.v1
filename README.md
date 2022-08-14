# Gitignore

create `.gitignore` automatically via `https://www.toptal.com/developers/gitignore`

## Requirements

`requests`

## Usage

```shell
python3 src/main.py --list
python3 src/main.py -l
python3 src/main.py python pycharm

alias gi="python3 ~/.../Gitignore/src/main.py"
gi --list/-l
gi --list/-l | grep py
```

## API

- list

  - https://www.toptal.com/developers/gitignore/api/list?format=lines

- get

  - https://www.toptal.com/developers/gitignore/api/python,pycharm+all
