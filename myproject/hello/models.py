from google.appengine.ext import ndb


class Greeting(ndb.Model):
    author = ndb.StringProperty()
    content = ndb.StringProperty()
    date = ndb.DateTimeProperty()
