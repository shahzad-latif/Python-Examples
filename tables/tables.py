number = input('Which table you want to print? ')
iNumber = int(number)
count = 1
while count <=1000:
    multiple = iNumber * count
    print(iNumber, 'x', count, ' = ', multiple)
    count = count +1

