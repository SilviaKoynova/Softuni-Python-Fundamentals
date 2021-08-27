n = int(input())
even_nums = []
odd_nums = []
positive_nums = []
negative_nums = []
for nums in range(n):
    numbers = int(input())
    if numbers % 2 == 0 or numbers == 0:
        even_nums.append(numbers)
    if not numbers % 2 == 0:
        odd_nums.append(numbers)
    if numbers >= 0:
        positive_nums.append(numbers)
    if numbers < 0:
        negative_nums.append(numbers)
word = input()
if word == 'even':
    print(even_nums)
elif word == 'odd':
    print(odd_nums)
elif word == 'positive':
    print(positive_nums)
elif word == 'negative':
    print(negative_nums)




