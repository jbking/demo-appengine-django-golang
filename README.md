# A demo sharing datastore beyond runtimes Python and Go in single Project on google appengine

# Python

myproject

## run on localhost

$ dev_appserver.py app.yaml

## deploy onto appengine

$ appcfg.py -A charged-state-106215 update app.yaml

# Go

gomod

Invoke the "/create" that create a greeting entity then it can be shown both runtimes(versions).

## run on localhost

$ goapp serve

## deploy onto appengine

$ goapp deploy -application charged-state-106215
