import os
def get_ak():
	"""
	what shall be done here is actually get aktk and add them to yum baseurl

	"""
	f=open("/var/axtu/asianux-auth","rw");
	print f.readline()
def exe_auth_client():
	os.system("/usr/share/axtu-authen-client/bin/axtu-authen-client-cui")
from yum.plugins import PluginYumExit, TYPE_CORE, TYPE_INTERACTIVE

requires_api_version = '2.3'
plugin_type = (TYPE_CORE, TYPE_INTERACTIVE)

def init_hook(conduit):
	conduit.info(2, 'Hello world')
	get_ak()
	exe_auth_client()
def postreposetup_hook(conduit):
	raise PluginYumExit('Goodbye')

