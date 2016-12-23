#!/usr/bin/python
#credit: python docs
import SimpleHTTPServer
import SocketServer
import threading
import subprocess
import time

PORT = 8054

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
