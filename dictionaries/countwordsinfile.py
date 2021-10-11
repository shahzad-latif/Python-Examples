datafile = open('data.txt', 'r')


count = dict()

for line in datafile:
    line = line.rstrip()
    words = line.split()
      
    for word in words:
        count[word] = count.get(word,0) + 1

bigword = None
bigcount = -1 

for k, v in count.items(): 
    if v > bigcount:
        bigword = k
        bigcount = v

print(bigword, bigcount)






