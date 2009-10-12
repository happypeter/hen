#http://www.faqs.org/docs/diveintopython/kgp_commandline.html
import sys
import getopt
def usage():
	print "I am usage()`"
def main(argv):                         
    grammar = "kant.xml"                 
    try:                                
        opts, args = getopt.getopt(argv, "hg:k:pd", ["help", "grammar="]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)                     

if __name__ == "__main__":
    main(sys.argv[1:])
