import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("enter url: ")
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
counts = tree.findall('.//count')
total = 0
for i in counts:
    total = total + int(i.text)
print (total)
