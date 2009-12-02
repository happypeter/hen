#!/usr/bin/python
import cgi
import os
form = cgi.FieldStorage()


print "Content-type: text/html"
html ="""
<hr>
<p>%s</p>
<hr>
"""

kw=form['keyword'].value
print html % ("search:: %s"%kw)
print "\n"
cmd="ls|grep "+kw
#print "running cmd: "+cmd
os.chdir("/var/www/")
out=os.popen(cmd).read()
if not out:
    print "<p>No matches</p>"

content1 = """
<a href="../%s">
"""
content2 = """
%s</a>
"""
file_list = out.split()
for file in file_list:
    print "<p>"
    print content1 %file
    file_name = file.replace(".html","")
    print content2 %file_name
    print "</p>"
# the position of html pages worth noting "../peter.html", that is the relative path to the .py file
#name = out.replace(".html")

