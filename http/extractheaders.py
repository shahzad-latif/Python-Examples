#This example creates a socket connection 
#gets the response from a web page
#and parses the resopnse to get response headers
#using regular expression
import socket
import re 

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

response = ''
while True:
    data = mysocket.recv(512)
    if(len(data) < 1):
        break
    #print(data.decode())
    result = re.findall('[a-zA-Z]+[-]*[a-zA-Z]*:\s.*', data.decode())
    if len(result) != 0:
        print(":::::::::::Full LIST:::::::::::")
        print(result)
        print(":::::::::::EACH HEADER:::::::::::")
        for item in result:
            print(item.rstrip())
    response = response + data.decode() 

print(":::::::::::Full RESPONSE:::::::::::")
print(response)
mysocket.close()


#result = re.findall('\s+:\S\s+', response)
#print(result)


