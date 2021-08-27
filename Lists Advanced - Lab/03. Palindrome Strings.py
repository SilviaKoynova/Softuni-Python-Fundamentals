words = input().split()
searched_palindrome = input()
palindromes = [word for word in words if word == word[::-1]]
count = palindromes.count(searched_palindrome)
print(palindromes)
print(f'Found palindrome {count} times')