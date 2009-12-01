import os
import sys
cui_exe ="/usr/share/axtu-authen-client/bin/axtu-authen-client-cui"
def read_user_info():
	# see ../read_user_info.py === conataining [pn. id, pw]
def generate_ak():
    #FIXME
    id, pw, pn = read_user_info()
    cmd = cui_exe+" -i "+ id + " -p "+ pw +" -n "+ pn
    os.system(cmd) #see edocs/AddAuth for details
def reg_or_acc():
	"""
	here we need to sent ak and hardware hash to auth_server 
	if ak is right, and HW hash matches: 
		generate tk
	else:
		call auth_client to register again
	
	NOTE: since we are going to change auth logic, so this fun is to be not implemented now	
	"""

def get_ak():
	"""
	what shall be done here is actually get aktk and add them to yum baseurl

	"""
        ak_file = "/var/axtu/asianux-auth"
        if os.path.exists(ak_file):
            if ak is not right:
                os.system(cui_exe+" -r") 
                #delete wrong ak, like above
                #and generate a new one, like below 
                generate_ak()
	f=open(ak_file,"rw");
	print f.readline()
        return f.readline()# maybe rstrip() is needed?
def get_tk():
	"""
        since auth_logic is going to be changed, so this fun is to be modified in the future
	since tk is quickly deleted by axtu, so some times this func will fail
	I am planning to change auth_client itself to make this garenteed
	"""
	# see ../get_tk.py

def change_url_for_yum():
	"""
	insert ak:tk to /etc/yum.repo.d/conf:baseurl
	"""
    #FIXME
def cleanup():
	"""
	before the plugin dies
	"""

from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE
requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def init_hook(conduit):
	conduit.info(2, 'Hello world')
	get_ak()
	get_tk()
	change_url_for_yum()
	cleanup()
def postreposetup_hook(conduit):
	raise PluginYumExit('Goodbye')

