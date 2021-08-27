nums_as_strings = [int(el) for el in input().split(', ')]
even = [index for index in range(len(nums_as_strings)) if nums_as_strings[index] % 2 == 0]
print(even)
