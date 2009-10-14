from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('starship.python.net',80))#110--- port num for POP mail server
sock.send('GET /\r\n')

print sock.recv(60)

