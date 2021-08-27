num_lines = int(input())
result = 0
for i in range(num_lines):
    char = str(input())
    result += ord(char)
print(f'The sum equals: {result}')
