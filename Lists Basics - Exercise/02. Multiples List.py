factor = int(input())
count = int(input())
number = 0
new_list = []
for nums in range(count):
    number += factor
    new_list.append(number)

print(new_list)
