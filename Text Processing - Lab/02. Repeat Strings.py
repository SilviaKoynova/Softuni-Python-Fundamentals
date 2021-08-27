words = input().split()
res = ''
for word in words:
    length = len(word)
    res += word * length
print(res)
