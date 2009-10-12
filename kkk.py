#here I want a html creator, doing 
# 1. read all the file name in a dir

import os

ooo=os.listdir('./')
#everything is read into list ooo
ooo.sort()#sorted items are easier to locate
os.makedirs("peter-html")#create dir to store all the output
f=open("./peter-html/index.html","w");
for s in ooo:
    f.write(s+"\n")

