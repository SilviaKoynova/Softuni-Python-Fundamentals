number = input().split()
number.sort(reverse=True)
print(''.join(str(i) for i in number))
