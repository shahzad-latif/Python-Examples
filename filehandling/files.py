datafile = open('data.txt', 'r')
print(datafile)

filecontent = datafile.read()
print(len(filecontent))

for line in datafile:
    print(line.rstrip())

