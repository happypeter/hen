#here I want a html creator, doing 
# 1. read all the file name in a dir

import os

ooo=os.listdir('./')
#everything is read into list ooo
print ooo[1]
os.makedirs("peter-html")#create dir to store all the output

