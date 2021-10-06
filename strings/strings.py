fruit = 'banana'

for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print(fruit[0:2])
print(fruit[3:4])
print(fruit[:3])
print(fruit[3:])

concat = 'hello' + fruit
print(concat)

concat = 'hello' + ' ' + fruit
print(concat)

concat = 3 * fruit
print(concat)

if 'n' in fruit:
    print('found n')

print(type(fruit))

print(dir(fruit))

if fruit == 'banana':
    print('banana Yes')

if fruit == 'apple':
    print('apple Yes')
else:
    print('apple No')

if 'a' > 'b':
    print('a > b')
else:
    print('a < b')

email = 'from user@gmail.com at 7 pm'
atpos = email.find('@')
print(atpos)
sppos = email.find(' ',atpos)
print(sppos)
host = email[atpos+1: sppos]
print(host)