#here "ak =3242" in the file asianux-auth
f=open("asianux-auth","rw");
l= f.readline()
print l
n=l[4:]
print n;

print n.replace("4","")
