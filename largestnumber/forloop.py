largest_so_far = -1
print('Before ', largest_so_far)

for num in [14, 28, 3, 16, 78, 6]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)

print('After ', largest_so_far)