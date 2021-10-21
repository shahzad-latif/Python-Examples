import requests
 
fhand = requests.get('https://www.py4e.com/code/romeo.txt')
print(fhand.text.strip())