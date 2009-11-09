#!/usr/bin/python
import os
import sys
if os.path.exists("ForMuse"):  #output files go here
      os.system("rm -rf ForMuse")
os.system("mkdir ForMuse")
if os.path.exists("filenames.txt"):
    os.system("rm filenames.txt")
os.system("ls pages>>filenames.txt") # "pages" is where all input files are in 
dirname = open("filenames.txt","r").read()
namelist = dirname.split("\n")
print "== ***********Ignore List************ =="
for name in namelist:
    if not name:
        break
    #try to get current number
    curfile = "pages/"+name+"/current"
    if not os.path.exists(curfile):
        print name+"     Ignored----NO current is found"
        continue   #if curfile is not there just ingnore this page, this means the page is empty
    curnum=open(curfile).read()
    filename ="pages/"+name+"/revisions/"+curnum
    filename = filename.replace("\n","")
    musefile = "ForMuse/"+name
    if not os.path.exists(filename):
        print name+"    Ignored----NO page in revisions/"
        continue  #the proper revision in current is not in revisions/, this happens when I delete this file already
    cmd = "cp " + filename + " " + musefile+ ".muse"
    os.system(cmd)
os.system("rm filenames.txt")
print "== ******************************* =="

