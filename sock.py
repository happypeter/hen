from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('mail.rmi.net',110))#110--- port num for POP mail server
print sock.recv(60)

