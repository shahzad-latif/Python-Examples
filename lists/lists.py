iList = [1, 5, 4, 2, 3]
sList = ['Banana', 'Apple', 'Orange']

print(iList)
print(sList)

print(len(iList))
print(len(sList))

print(min(iList))
print(min(sList))

print(max(iList))
print(max(sList))

print(sum(iList))
#print(sum(sList)) #Not supported

iList.sort()
sList.sort()
print(iList)
print(sList)

iList.reverse()
sList.reverse()
print(iList)
print(sList)

iList.append(7)
sList.append('Grapes')
print(iList)
print(sList)

iList.remove(7)
sList.remove('Grapes')
print(iList)
print(sList)


