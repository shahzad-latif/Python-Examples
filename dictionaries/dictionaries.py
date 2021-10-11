from typing import List


purse = dict()
purse['cash'] = 100
purse['candy'] = 10
purse['tissue'] = 5

print(purse)

print(purse['cash'])

purse['cash'] = purse['cash'] + 100

print(purse['cash'])


count = dict()
names = ['John', 'Rohn', 'Mohn', 'Rohn', 'John', 'Mohn', 'Mohn']

for name in names:
    count[name] = count.get(name,0) + 1

print(count)

print(list(count))

print(count.keys())
print(count.values())
print(count.items())