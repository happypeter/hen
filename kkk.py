#here I want a html creator, doing 
# 1. read all the file name in a dir

import os
import sys
ooo=os.listdir('./')
#everything is read into list ooo
ooo.sort()#sorted items are easier to locate
os.makedirs("peter-html")#create dir to store all the output
os.makedirs("peter-html/html")
f=open("./peter-html/index.html","w");
for s in ooo:
    os.system("cp " + s + " " + s + ".html")
    f.write('<a href="./html/')
    f.write(s+".html")
    f.write('">')
    f.write(s)
    f.write('</a>---<br>\n')

os.system("mv  *.html ./peter-html/html/")

