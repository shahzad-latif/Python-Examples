import xml.etree.cElementTree as ET

data = '''<system><users>
<user id="1">
 <name>User A</name>
 <age>25</age>
</user>
<user id="2">
 <name>User B</name>
 <age>36</age>
</user>
</users>
</system>'''

tree = ET.fromstring(data)
users = tree.findall('users/user')
print(users)
for user in users:
    print('ID: ', user.get('id'))
    print('Name: ', user.find('name').text)
    print('Age: ', user.find('age').text)
    


