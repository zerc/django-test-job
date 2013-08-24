Django small test job
=====================

Just a test job to show example of my code.

### Install
    sudo apt-get install python-pip, sqlite3
    sudo pip install virtualenv

    git clone git@github.com:zerc/django-test-job.git test-django-job
    cd test-django-job
    virtualenv venv
    . venv/bin/activate
    pip install -r pip.req

Add superuser:

    ./manage.py createsuperuser


Runserver:

    ./manage.py runserver 0.0.0.0:8000

And go to *http://localhost:8000/admin/*

### Blog app
This simples blog app with tags and comments (from box). Not so good solution, but easy and fast develop. Just for show example of.

Run migrations:

    ./manage.py migrate


Run syncdb for add comments tables:

    ./manage.py syncdb

Apply fixtures:

    ./manage.py loaddata initial.json

Run tests if you whant:

    ./manage.py test blog
    
Start server and got to posts main page: *http://localhost:8000/posts/*
