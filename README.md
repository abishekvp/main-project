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
>import os<br/>
>try:import requests<br/>
>except:<br/>
>    os.system("pip install requests")<br/>
>    import requests<br/>
>try:from zipfile import ZipFile<br/>
>except:<br/>
>    os.system("pip install zipfile")<br/>
>    from zipfile import ZipFile<br/>
>def download_file():<br/>
>    url = "https://github.com/abishekvp/django/archive/refs/heads/master.zip"<br/>
>    file = requests.get(url, allow_redirects=True)<br/>
>    open('django.zip', 'wb').write(file.content)<br/>
>    with ZipFile("E:\\Desktop\\Dj-auto\\django.zip", 'r') as zFile:zFile.extractall(path="E:\\Desktop\\Dj-auto\\")<br/>
>    os.rename("django-master","django")<br/>
>    os.remove("E:\\Desktop\\Dj-auto\\django.zip")<br/>
>def git():<br/>
>    os.system("git init")<br/>
>    os.system("git clone https://github.com/abishekvp/django.git")<br/>
>def run_project():<br/>
>    os.chdir(os.path.expanduser('django'))<br/>
>    os.system("pip install -r requirements.txt")<br/>
>    os.system("python -m manage runserver")<br/>
>def main(inp):<br/>
>    if inp=="Yes":<br/>
>        git()<br/>
>        run_project()<br/>
>    else:<br/>
>        download_file()<br/>
>        run_project()<br/>
>inp = input("Do you have git?\n1.Yes  2.No\nJust enter for Yes (Yes)") or "Yes"<br/>
>main(inp)<br/>
</pre>
