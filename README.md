Note:   &::  -it's a comment

- install python

given below commands all work in windows command prompt

only on initial deployment,
follow commands in cmd as in project location

>pip install virtualenv &::to install python package for creating virtual environment <br/>
>python -m venv env  &::to create virtual environment <br/>
>env\scripts\activate  &::to activating virtual environment <br/>
>pip install -r requirements.txt  &::to install requirements on virtual environment <br/>
>python manage.py runserver  &::to run server <br/>

to deactivate the environment
>env\scripts\deactivate

for regular host - locally
>env\scripts\activate  &::only if environment is not activated <br/>
>python manage.py runserver  &::to host project


*ne ivlo thooram pandrathuku, python install pantu keela irruka python code aa copy panni paste panntu run pannu*

<pre>
import os
try:import requests
except:
    os.system("pip install requests")
    import requests
try:from zipfile import ZipFile
except:
    os.system("pip install zipfile")
    from zipfile import ZipFile
def download_file():
    url = "https://github.com/abishekvp/django/archive/refs/heads/master.zip"
    file = requests.get(url, allow_redirects=True)
    open('django.zip', 'wb').write(file.content)
    with ZipFile("E:\\Desktop\\Dj-auto\\django.zip", 'r') as zFile:zFile.extractall(path="E:\\Desktop\\Dj-auto\\")
    os.rename("django-master","django")
    os.remove("E:\\Desktop\\Dj-auto\\django.zip")
def git():
    os.system("git init")
    os.system("git clone https://github.com/abishekvp/django.git")
def run_project():
    os.chdir(os.path.expanduser('django'))
    os.system("pip install -r requirements.txt")
    os.system("python -m manage runserver")
def main(inp):
    if inp=="Yes":
        git()
        run_project()
    else:
        download_file()
        run_project()
inp = input("Do you have git?\n1.Yes  2.No\nJust enter for Yes (Yes)") or "Yes"
main(inp)
</pre>
