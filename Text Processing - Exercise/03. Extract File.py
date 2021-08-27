url_file = input().split("\\")
answer = url_file[-1]
final = answer.split('.')
print(f'File name: {final[-2]}')
print(f"File extension: {final[-1]}")
