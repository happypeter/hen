#!/usr/bin/python

#  Problem
import os
import sys
def checkCamel(w):
    if len(w)<4:
        return False
    if not w[0].isupper():
        return False
    if w[1].isupper():
        return False
    if w[2:].isupper() or w[2:].islower():#means still anthoer Upper case letter
        return False
    return 1   #False
os.system("ls edocs>filename.txt")
names = open("filename.txt").read()
namelist = names.split("\n")
for name in namelist:
    print name
    fullname = "edocs/"+name
    file = open(fullname,"r").read()
    file = file.replace("<<TableOfContents>>","")#maybe <contents> is also nice
    file = file.replace("<<BR>>","")
    file = file.replace("{{{","<example>")
    file = file.replace("}}}","</example>")

    #below is for the sake of getting clean words, the fileFF should not be saved
    fileFF = file.replace("."," ")
    fileFF = fileFF.replace(")"," ")
    fileFF = fileFF.replace("\n"," ") # maybe we can try rstrip() to avoid ^M problem
    wordlist = fileFF.split(" ")
    sys.stdout = open(name,'a')
    for word in wordlist: # check CamelWords embrace them [[]]
        bool = checkCamel(word)
        if bool:
            print word
            link="[["+word+"]]"
            print link
            file = file.replace(word,link)
    print file
#remove some garbage

