import os

cui_exe ="/usr/share/axtu-authen-client/bin/axtu-authen-client-cui"
def read_user_info():
	print "Plz input the product number:"#userid and passwd as well
	product_num = sys.stdin.readline()
	print "the num is:"
	print product_num
	# return a list, conataining [pn. id, pw]
def generate_ak():
    #FIXME
    info_list = read_user_info()
    cmd = cui_exe+" -i "+info_list[0]+" -p "+info_list[1]+" -n "+info_list[2]
    os.system(cmd) #see edocs/AddAuth for details
def get_ak():
	"""
	what shall be done here is actually get aktk and add them to yum baseurl

	"""
        ak_file = "/var/axtu/asianux-auth"
        if os.path.exists(ak_file):
            if ak is not right:
                os.system("/usr/share/axtu-authen-client/bin/axtu-authen-client-cui -r") 
                #delete wrong ak, like above
                #and generate a new one, like below 
                generate_ak()
	f=open(ak_file,"rw");
	print f.readline()
        return f.readline()# maybe rstrip() is needed?

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

