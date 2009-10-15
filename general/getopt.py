import getopt
import sys
def main(argv):                         
    grammar = "kant.xml"    
    try:                                
        opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="]) 
    except getopt.GetoptError:     
        usage()           
        sys.exit(2)     
if __name__ == "__main__":
    main(sys.argv[1:])  
