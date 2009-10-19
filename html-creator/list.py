#with this module, we will be able to handle subdirs
import os
def lister(dummy, dirname, filesindir):
    print '[' + dirname + ']'
    for fname in filesindir:
        path = os.path.join(dirname, fname)
        if not os.path.isdir(path):
            print path

os.path.walk('.', lister, None)
