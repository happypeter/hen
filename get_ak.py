#here "ak =1243" in the file asianux-auth
f=open("asianux-auth","r");
l= f.readline()
print l
n=l[4:]
print n;

ll=n.replace("4","")
f=open("dup_asianux-auth","w");
f.write(ll)
