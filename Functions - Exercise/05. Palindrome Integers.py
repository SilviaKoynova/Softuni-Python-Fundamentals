def is_palindrome(numbers):
    for numbers in numbers:

        if numbers == numbers[::-1]:
            print('True')
        else:
            print('False')


num = input().split(', ')
is_palindrome(num)
