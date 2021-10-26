import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"
address = "shed 99 lahore pakistan"
#use your own key. the below key is destroyed :)
key = "AIzaSyAUuWX....2yDyU....bz-GeT7pzOi7xRME"

url = serviceurl + urllib.parse.urlencode({'address':address}) + "&" + urllib.parse.urlencode({'key':key})

#print(url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()

#print(len(data))

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('Failed to retreive')
    print(data)
    exit    

print(json.dumps(js, indent=4))

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
location = js["results"][0]["formatted_address"]

print("Lat", lat, "Lng", lng, "Location", location)



