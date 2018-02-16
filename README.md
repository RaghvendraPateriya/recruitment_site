Project Description
===================

Build a rudimentary recruitment site that exposes the following functionality:

- A page that allows anonymous users to submit applications
- A restricted administration page where admins can:
    - view applications
    - reject applications
    - accept applications

Installation
============

Create virtual Environment:

```
$ virtualenv dev
$ source dev/bin/activate
$ pip install -r requirement.txt
```

Setup Django Project
====================

Go to(```cd```) the directory where 'manage.py', after run below command in shell.

```
$ python manage.py createsuperuser --username admin --email admin@admin.com

<set password>
```

Run Project
===========

```
$ python manage.py runserver
```

Point your browser 127.0.0.1:8000


URLs
====

- Application Submit form: http://localhost:<port> eg. http://127.0.0.1:8000
- Administration Page: http://localhost:<port>/admin eg. http://127.0.0.1:8000/admin
  pass those credential which we use at command "python manage.py createsuperuser --username admin --email admin@admin.com"
