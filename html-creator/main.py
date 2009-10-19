#here I want a html creator, doing 
# 1. read all the file name in a dir
# 2. wirite all the names into ./peter-html/index.html
# 3. add links
# TODO:
# 1. add sth like <go to homepage> into each file
# 2. and all the other good tags for general use
# 3. read out the first line of each file as its desc in index.html
import os


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
dir=os.popen("python ./list.py").read()
print dir
listtt=dir.split('\n')
print "ppppppppppp"
print listtt

ooo=os.listdir('./')
#everything is read into list ooo
ooo.sort()#sorted items are easier to locate

#create dir to store all the output
#ensure_dir("./peter-html")
#ensure_dir("./peter-html/html")
os.makedirs("./peter-html")
os.makedirs("./peter-html/html")
   
f=open("./peter-html/index.html","w");
f.write("<h1>Index</h1>")
for s in ooo:
    os.system("cp "+s+" "+s+".txt")
#we use .txt rather than .html as extention
#thus we do not need add <pre> into the files to make lines stand in different line
    f.write('<a href="./html/')
    f.write(s+".txt")
    f.write('">')
    f.write(s)
    f.write('</a><br>\n')
f.close() #close index.html
os.system("mv  *.txt ./peter-html/html/")

ppp=os.listdir('./peter-html/html/')
for ss in ppp:
    print ss
    #we want to add some tags into each file to make them pretty
