import json

data = '''[
{
    "id":"1",
    "name": "User A",
    "age": "25"
},
{
    "id":"2",
    "name": "User B",
    "age": "35"
}
]'''

users = json.loads(data)

for user in users:
    print('ID: ', user['id'])
    print('Name: ', user['name'])
    print('Age: ', user['age'])



