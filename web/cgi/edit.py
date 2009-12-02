#!/usr/bin/python
import cgi
import os
import urllib
form = cgi.FieldStorage()


print "Content-type: text/html"
html ="""
<hr>
<p>%s</p>
<hr>
"""

kw=form['bt_name'].value
print html % ("I am going to open------ %s"%kw)


header = """
<form method=POST action="save.py">
<input class="button" type="submit" name="button_save" value="%s" onClick="flgChange = false;">

<textarea id="editor-textarea" name="savetext" lang="en" dir="ltr" rows="50" cols="150"
          onChange="flgChange = true;" onKeyPress="flgChange = true;">

"""

footer = """

</textarea>

</form>

"""
file_name = "/home/pet/edocs/"+kw+".muse"
print header %kw
print open(file_name,"r").read()
print footer
name = os.popen('whoami').read()
print "the usr of the cgi is :"+name

