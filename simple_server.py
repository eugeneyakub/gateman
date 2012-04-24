#! /usr/bin/env python

import sys
from subprocess import call

import urllib2
import json
# Whatever structure you need to send goes here:



request= ''
call(['touch', '/home/eugene/t'])
    


request = ''
while True:
  data = sys.stdin.readline().strip()
  request = request + data + '<br>'
  if data == "":
    print 'HTTP/1.0 200 OK'
    print 'Access-Control-Allow-Origin: *'
    print 'Access-Control-Allow-Headers: X-Prototype-Version, X-Requested-With, Content-type, Accept'
    print 'Access-Control-Allow-Methods:  GET, POST, OPTIONS, PUT'
    print '<html><body><p>'+request+'</p></body></html>'
    sys.stdout.flush()
    break
