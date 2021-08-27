def calculator(op, num1, num2):
    if op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        return num1 // num2
    elif op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2


operator = input()
a = int(input())
b = int(input())
result = calculator(operator, a, b)
print(result)
