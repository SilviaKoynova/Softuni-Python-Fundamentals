def sum_number(num1, num2):
    return num1 + num2


def subtract(sum_of, num3):
    return sum_of - num3


def solve(num1, num2, sum_of):
    sum_of_two = sum_number(first_num, second_num)
    res = subtract(sum_of_two, third_num)
    return res


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = solve(first_num, second_num, third_num)
print(result)
