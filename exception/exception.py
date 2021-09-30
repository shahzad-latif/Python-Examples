inpage = input("What is your age? ")
try:
    age = int(inpage)
except:
    age = -1

if age == -1:
    print("Please enter proper age value.")
elif age <= 40:
    print("You're young.")
elif age <= 55:
    print("You're middle aged.")
else:
    print("You're old")
    
print("Age: ", age)