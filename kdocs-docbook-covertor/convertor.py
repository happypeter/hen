import os
ooo=os.listdir('/home/pet/kdocs')
#everything is read into list ooo
ooo.sort()#sorted items are easier to locate

print ooo

#os.makedirs("./docbook-kdocs")

f=open("./kdocs.xml","w");
msg = """
<?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN" "http://docbook.org/xml/4.2/docbookx.dtd">
 <book>
      <title>kdocs</title>

"""
f.write(msg)

