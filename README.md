Note:   &::  -it's a comment

- install python

given below commands all work in windows command prompt

only on initial deployment,
follow commands in cmd as in project location

> pip install virtualenv &::to install python package for creating virtual environment__
> python -m venv env  &::to create virtual environment__
> env\scripts\activate  &::to activating virtual environment__
> pip install -r requirements.txt  &::to install requirements on virtual environment__
> python manage.py runserver  &::to run server__

to deactivate the environment
> env\scripts\deactivate

if only normal host
> env\scripts\activate  &::if environment is not activated to activate__
> python manage.py runserver  &::to run server

