import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

address = input('Enter location: ')

#url = urllib.parse.urlencode({'address': address})
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')

sum=0
count=0
for i in counts:
    sum+=int((i.text))
    count+=1
print('Count: ',count)
print('Sum: ',sum)
