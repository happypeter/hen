#!/usr/bin/python
import os
import sys
if os.path.exists("Edocs"):  #output files go here
      os.system("rm -rf Edocs")
os.system("mkdir Edocs")
if os.path.exists("filenames.txt"):
    os.system("rm filenames.txt")
os.system("ls ForMuse>>filenames.txt") # "ForMuse" is where all input files are in 
dirname = open("filenames.txt","r").read()
namelist = dirname.split("\n")
print "== ***********Ignore List************ =="
for name in namelist:
    if not name:
        break
    #try to get current number
    musefile = "ForMuse/"+name
    if not os.path.exists(musefile):
        print name+"     Ignored----NOT found"
        continue   #if file is not there just ingnore this page, this means the page is empty
    content = open(musefile).read()
    content = content.replace("<<TableOfContents>>","")
    content = content.replace("<<BR>>","")
    content = content.replace("<<TableOfContents>>","")
    content = content.replace("{{{","<example>")
    content = content.replace("}}}","</example>")
    # the sequence is fatal for the following substitution
    content = content.replace("*","-")
    content = content.replace("=","*")

    musefile2 = "Edocs/"+name #musefle2 the fomatted output files
    if os.path.exists(musefile2):
        print name+" Already there!!! Not overwriting ..."
        continue  #the proper revision in current is not in revisions/, this happens when I delete this file already
    f = open(musefile2,"w")
    f.write(content)
os.system("rm filenames.txt")
print "== ******************************* =="

