import urllib.request, urllib.parse, urllib.error
import json

url = input("enter url: ")
libhandle = urllib.request.urlopen(url)
data = libhandle.read().decode()
info = json.loads(data)
print(json.dumps(info,indent=4))
total = 0
for x in info["comments"]:
    total = total + x["count"]
print(total)
