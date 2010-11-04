import datetime
import logging
import os
import random
from django.utils import simplejson
from google.appengine.api import channel
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.deferred import deferred
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app


def create_channel_id():
  return channel.create_channel("sweet")

def send(message):
    channel.send_message("sweet", simplejson.dumps(message))

class PingEm(webapp.RequestHandler):

    def get(self):
        send('This is cool ')
        send('Really cool')
        
class MainPage(webapp.RequestHandler):

    def get(self):
        id = create_channel_id()
        template_values = {'channel_id': id,}
        path = os.path.join(os.path.dirname(__file__), 'test.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/a', PingEm)
                                     ], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
