import json

data = '''{
"name": "Person's Name",
"phone": "+123456789",
"email": {
    "hide": "yes"
    }
}'''

tree = json.loads(data)

print('Name: ', tree["name"])
print('Phone: ', tree["phone"])
print('Hide: ', tree["email"]["hide"])


