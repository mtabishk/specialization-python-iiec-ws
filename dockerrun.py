#!/usr/bin/python3

print("content-type: text/html")
print()

print("<html>")
print("<head><title>CGI Program</title></head>")
print("<body>")
print("<body bgcolor='#C0C0C0'>")
print("<h1>Docker Backend</h1>")
print("\n\n")

import cgi
import subprocess as sp

form = cgi.FieldStorage()

osname = form.getvalue("x")

image = form.getvalue("i")

cmd = "sudo docker run -dit --name {0} {1}".format(osname,image)

output = sp.getstatusoutput(cmd)
status = output[0]
out = output[1]

if status==0:
    print("<b>Container: {0} is launched...</b>".format(osname))
    dps = "sudo docker ps -a"
    odps = sp.getoutput(dps)
    print("<pre>")
    print("<p>"+odps+"</p>")
    print("</pre>")
else:
    print("<b>Some Error occured: {}<b>".format(out))
print("</body>")
print("</html>")
