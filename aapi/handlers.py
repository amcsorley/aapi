#!/usr/bin/python

import time
import ConfigParser

from tornado.web import RequestHandler
from tornado.escape import json_encode

config = ConfigParser.ConfigParser()
config.read('/etc/aapi/aapi.conf')
logdir = config.get('defaults', 'logdir')
port = config.get('defaults', 'port')
apikeyfile = config.get('defaults', 'apikeyfile')

class Help(RequestHandler):
    def get(self):
        """Print available functions"""
        result = { 'Help' : 'Print available functions' }
        self.write(result)

def do_thing():
    output = time.ctime()
    return output

class DoJsonpThing(RequestHandler):
    def get(self):
        """Do the jsonp thing"""
        result = { 'thing' : do_thing() }
        callback = self.get_argument('callback')
        jsonp = "{jsfunc}({json});".format(jsfunc=callback,json=json_encode(result))
        self.set_header('Content-Type', 'application/javascript')
        self.write(jsonp)

class DoJsonThing(RequestHandler):
    def get(self):
        """Do the json thing"""
        result = { 'thing' : do_thing() }
        json = json_encode(result)
        self.set_header('Content-Type', 'application/json')
        self.write(json)


