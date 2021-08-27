divisor = int(input())
bound = int(input())
for i in range(divisor, bound + 1):
    if i % divisor == 0:
        if i <= bound:
            greater_num = i
print(greater_num)
