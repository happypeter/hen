import os
import sys
def read_user_info():
        info_list = []
        print "Plz input your userID:"
        id = sys.stdin.readline()
        id = id.rstrip()#remove the trailing "\n"
        info_list.append(id)

        print "Plz input your passwd:"
        pw = sys.stdin.readline()
        pw = pw.rstrip()
        info_list.append(pw)

        print "Plz input the product number:" #userid and passwd as well
        pn = sys.stdin.readline()
        pn = pn.rstrip()
        info_list.append(pn)
    
        return info_list

id, pw, pn = read_user_info()

print "now the result is:"

print id + " " + pw + " " + pn
