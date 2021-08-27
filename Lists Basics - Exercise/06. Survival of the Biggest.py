numbers = input().split()
new_list = []
for num in numbers:
    new_list.append(int(num))
n = int(input())
for _ in range(n):
    new_list.remove(min(new_list))
print(new_list)
