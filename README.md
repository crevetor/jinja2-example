Jinja example
=============

A small program that takes a jinja template file and some variables as input and outputs a rendered template.

Installation
------------

This program depends on click and jinja2. It uses pipenv to manage those dependencies.
* Install pipenv
* Run : ```pipenv install``` in the project directory
* You can now run the program with ```pipenv run python main.py```

Usage
-----

This uses the provided example.tpl :
```pipenv run python main.py -t example.tpl -o rendered.txt -v var1=value1 -v var2=value2```
Will generate a file called rendered.txt with var1 and var2 replaced with value1 and value2 respecitvely.
