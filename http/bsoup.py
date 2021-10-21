#use BeautifulSoup to parse HTML pages
from bs4 import BeautifulSoup
import requests
 
html = requests.get('https://www.dr-chuck.com/page1.html').text.strip()
#print(html)

soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

for tag in tags:
    print(tag.get('href',None))


