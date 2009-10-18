from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('starship.python.net',80))#110--- port num for POP mail server
sock.send('GET /\r\n')

print sock.recv(10)

#now I have all the html tags and everthing, there are a lot I can do
#e.g I can define my own tag <peter-data></peter-data>
#then when I get the tag on my client, I can code to do anything to it
#before send the page to firefox
