#here I want to say how command line works
#this file should be merged into auth.py later
#argecho.py
import sys
import os
def exe_auth_client(arg):
	s = "ls"
	s_arg= s+" "+arg
        os.system(s_arg)

exe_auth_client(sys.argv[1])

