text = input()
numbers_str = text.split()
new = []
for num in numbers_str:
    number = -int(num)
    new.append(number)
print(new)
