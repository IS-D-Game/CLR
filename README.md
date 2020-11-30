# Introduction

The goal of this project is to implement a City-River-Country game as a learning experience. 

STOP is written with django 3.1.2 and python 3.


### Main features

* ???

* ???

* ???

* SQLite by default if no env variable is set

# Usage

To use this game:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django and bootstrap by running

    $ pip install django
    $ pip install django-bootstrap4
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject stop
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    $ pip3 install django-bootstrap4
    
And then:

    $ python3 -m django startproject stop
      
      
After that just install the local dependencies, run migrations, and start the server.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/IS-D-Game/CLR.git
    $ cd {{ stop }}
    
    
Activate the virtualenv for your project.

For Windows User 

    $ venv\Scripts\activate
    
For OS User

    $ source bin/activate
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the server:

    $ python manage.py runserver
