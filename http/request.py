#This example creates a socket connection 
#and gets the response from a web page
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

response = ''
while True:
    data = mysocket.recv(512)
    if(len(data) < 1):
        break
    response = response + data.decode() 

print(":::::::::::Full RESPONSE:::::::::::")
print(response)
mysocket.close()




