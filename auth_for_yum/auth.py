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

def change_url_for_yum():
    #FIXME
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE

requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def init_hook(conduit):
	conduit.info(2, 'Hello world')
	get_ak()
	change_url_for_yum()
def postreposetup_hook(conduit):
	raise PluginYumExit('Goodbye')

