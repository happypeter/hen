#from P723 Programming Python
import sys
from socket import *
serverHost = 'localhost'
serverPort = 5009

msg = ['hello peter']
if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) >2:
        message = sys.argv[2:]
sock =socket(AF_INET, SOCK_STREAM)
sock.connect((serverHost, serverPort))

for l in msg:
    sock.send(l)
    data = sock.recv(1024)
    print 'client side received:', repr(data)

sock.close()

