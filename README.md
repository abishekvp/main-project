Note:   &::  -it's a comment

- install python

given below commands all work in windows command prompt

only on initial deployment,
follow commands in cmd as in project location

>pip install virtualenv &::to install python package for creating virtual environment
>python -m venv env  &::to create virtual environment
>env\scripts\activate  &::to activating virtual environment 
>pip install -r requirements.txt  &::to install requirements on virtual environment
>python manage.py runserver  &::to run server

to deactivate the environment
>env\scripts\deactivate

if only normal host
>env\scripts\activate  &::if environment is not activated to activate
>python manage.py runserver  &::to run server

