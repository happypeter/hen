from socket import *
myHost=''
myPort=5009
sock=socket(AF_INET, SOCK_STREAM)
sock.bind((myHost,myPort))
sock.listen(5)

while True:
    connection, adress = sock.accept()
    print "server connnected by", adress
    while True:
        data = connection.recv(1024)
        if not data: break
        connection.send("echo--->"+data)
    connection.close()
