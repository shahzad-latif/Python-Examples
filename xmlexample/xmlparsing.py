import xml.etree.cElementTree as ET

data = '''<person>
<name>Person's Name</name>
<phone>+123456789</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)

print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))


