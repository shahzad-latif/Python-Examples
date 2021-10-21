import urllib.request, urllib.parse, urllib.error
#from urllib.request import urlopen

fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhandle:
    print(line.decode().strip())



