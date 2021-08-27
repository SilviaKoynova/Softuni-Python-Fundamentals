nums_str = input().split(', ')
count = int(input())
nums = []
for num in nums_str:
    nums.append(int(num))
result_sum = [0] * count
for i in range(len(nums)):
    index = i % count
    result_sum[index] += nums[i]
print(result_sum)
# numbers = input().split(', ')
# beggars = int(input())
# sums = [0] * beggars
# while numbers:
#     for beggar in range(beggars):
#         if not numbers:
#             break
#         sums[beggar] += int(numbers.pop(0))
# print(sums)
