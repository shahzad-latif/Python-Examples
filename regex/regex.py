import re

data = "My 2 favorite numbers are 14 and 30"

#get all numbers having one or more digits
result = re.findall('[0-9]+', data)

print(result)

#find all upper case vowels
result = re.findall('[AEIOU]+', data)

print(result)

#find all lower case vowels
result = re.findall('[aeiou]+', data)

print(result)

#find all words starting with f having any number of 
#letters and ending with a space till the last space!!
# .+ greedy search!
result = re.findall('f.+\s', data)

print(result)

# ? makes it not greedy! so first occurance would be enough
result = re.findall('f.+?\s', data)
print(result)

#get @ with before and after any non space characters
data = "From username@domain.com at 3:00 PM"
result = re.findall('\S+@\S+', data)
print(result)

result = re.findall('@([^ ]*)', data)
print(result)