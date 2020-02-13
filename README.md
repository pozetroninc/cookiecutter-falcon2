# Cookiecutter Falcon 2.0

This guide should get you started with Falcon 2.0 projects quickly by using the wonderful cookicutter.

### Cookiecutter
Cookiecutter is a command-line utility that creates projects from cookiecutters (project templates), e.g. creating a Python package project from a Python package project template.

### Install cookiecutter
It's simple, you only need to install python package:
```
pip install cookiecutter
```
Now you can create new projects using your new favourite template.

### Get the template
You need to clone the git repository:
```
git clone https://github.com/pozetroninc/cookiecutter-falcon2.git
```

### Create skeleton
To create the skeleton you need to indicate to cookiecutter where the template is:
```bash
cd cookiecutter-falcon
cookiecutter .
```

The tool is interactive and it will request for some information as:
* project_name
* project_slug
* author_name
* author_mail
* project_description [A short description of the project.]
* project_url [example.com]
* use_docker
* use_mongodb
* use_redisdb
* Select open_source_license or not open source

Note: The project_name should not contain spaces or other characters which aren't valid directory names.

When finished, a folder in the current directory with the name of selected "project_name" step given is created. You only need to move it where you want it lives:

```
cd my-project
tree .
.
├── my-project
│   ├── app.py
│   ├── __init__.py
│   ├── sample
│   │   ├── __init__.py
│   │   └── models.py
│   └── settings
│       ├── base.py
│       ├── docker.py
│       ├── __init__.py
│       ├── local.py
│       └── production.py
├── docker
│   ├── falcon-docker-entrypoint.sh
│   └── FalconDockerfile
├── docker-compose.yml
├── README.rst
├── requirements
│   ├── dev-requirements.txt
│   ├── requirements.txt
│   └── test-requirements.txt
├── setup.py
└── tox.ini

5 directories, 18 files
```

Note: This project is a fork of the original project for Falcon 1.0 projects at https://github.com/7ideas/cookiecutter-falcon
This fork changes very little and the majority of the work is directly attributable to the folks at 7ideas.
