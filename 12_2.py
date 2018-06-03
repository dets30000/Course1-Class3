from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count=int(input('Enter count: '))
position=int(input('Enter position: '))
print('Retrieving: ',url)

#html = urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, "html.parser")

names=list()
counter=0
namedb=list()
weblist=list()

#http://py4e-data.dr-chuck.net/known_by_Prentice.html
#http://py4e-data.dr-chuck.net/known_by_Fikret.html
i=0
for i in range(0,count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')

    counter=0

    for tag in tags:
        if counter == position -1 :
            url=tag.get('href',None)
            print('Retrieving: ',url)
            break
        counter+=1
