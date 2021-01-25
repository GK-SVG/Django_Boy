# Install MongoDB 
https://docs.mongodb.com/compass/current/install

# Watch this Video 
https://www.youtube.com/watch?v=MiS6y9kffBs


## Getting Started with Django
The clean, fast and right way to start a new <a href="https://docs.djangoproject.com/en/3.0/intro/tutorial01/">Django</a>`3.0.7` powered website.

## Getting Started with Project

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ python3 -m venv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/GK-SVG/repo-name/archive/master.zip projectname

$ cd projectname/
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).

* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
