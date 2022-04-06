
Services through Backend, for documentation please refer schema on swagger link
### Tech Used




* [FastAPI](https://fastapi.tiangolo.com) - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.


### Installation

python]([https://www.python.org/](https://www.python.org/)) v3+ to run.

Install the dependencies and devDependencies and start the server.

Go in directory where you want to setup project, Create virtual environment
```sh
$ virtualenv env -p python3
```
Clone Project
```sh
$ git clone [project_url]
```
Go to project directory
```sh
$ cd project_directory
$ pip install -r requirements.txt
```

run the following command on mysql

DROP DATABASE IF EXISTS ev;

CREATE DATABASE ev DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

Now everything is setup & ready to run
```sh
$ uvicorn main:fastApp --reload --host 0.0.0.0