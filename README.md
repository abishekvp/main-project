Note:   &::  -it's a comment

- install python

given below commands all work in windows command prompt

only on initial deployment,
follow commands in cmd as in project location

-> pip install virtualenv &::to install python package for creating virtual environment
-> python -m venv env  &::to create virtual environment\n
-> env\scripts\activate  &::to activating virtual environment\n 
-> pip install -r requirements.txt  &::to install requirements on virtual environment\n
-> python manage.py runserver  &::to run server\n

to deactivate the environment
-> env\scripts\deactivate

if only normal host
-> env\scripts\activate  &::if environment is not activated to activate\n
-> python manage.py runserver  &::to run server

