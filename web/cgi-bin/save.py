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

kw=form['savetext'].value
print html % ("I am going to save: %s"%kw)
print "\n"
file = form['button_save'].value
file_name = "/home/pet/edocs/"+file+".muse"
open(file_name,"w").write(kw)
