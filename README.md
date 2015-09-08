# An experimental miscellaneous code for google appengine

- sharing datastore beyond runtimes Python and Go in single project
- django admin with django-nonrel

# Python

myproject

## run on localhost

$ ./manage.py runserver

## deploy onto appengine

$ ./manage.py deploy --application=charged-state-106215

# Go

gomod

Invoke the "/create" that create a greeting entity then it can be shown both runtimes(versions).

## run on localhost

$ goapp serve

## deploy onto appengine

$ goapp deploy -application charged-state-106215
