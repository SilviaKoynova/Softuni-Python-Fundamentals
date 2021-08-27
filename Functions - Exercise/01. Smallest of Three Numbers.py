def smallest_num(a, b, c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    if c <= a and c <= b:
        return c


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_num(first_number, second_number, third_number)
print(result)
