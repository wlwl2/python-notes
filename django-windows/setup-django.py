"""
## Uses
Python 3.6
MySQL Server 5.7
Windows 10

## Install

Set path to C:\Program Files\MySQL\MySQL Server 5.7\bin to
access mysql command from cmd prompt.

In terminal:
mysql -u root -p

CREATE DATABASE testdb CHARACTER SET utf8;

Probably better to create a new username and password
instead of using root username and password.

In settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 'portnumber',
    }
}

Now you can run:
python manage.py migrate

"""
