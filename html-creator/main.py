#here I want a html creator, doing 
# 1. read all the file name in a dir
# 2. wirite all the names into ./peter-html/index.html
# 3. add links
# TODO:
# 1. add sth like <go to homepage> into each file
# 2. and all the other good tags for general use
# 3. read out the first line of each file as its desc in index.html
import os
html_tab="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"
dir=os.popen("python ./list.py").read()
dir = dir.replace('[','')
dir = dir.replace(']','')
listtt=dir.split('\n')
print listtt

f=open("index.html","w");
f.write("<h1>Index</h1>")
for s in listtt:
    lists = s.split('/')
    n = len(lists)
    f.write(n*html_tab)
    f.write('<a href="')
    f.write(s)
    f.write('">')
    ss=lists[n-1]
    f.write(ss)
    f.write('</a><br>\n')
f.close() #close index.html

