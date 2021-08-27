def sum_of_all_even_odd(number1):
    sum_even = 0
    sum_odd = 0
    for num in number1:
        number = int(num)
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number
    print(f'Odd sum = {sum_odd}, Even sum = {sum_even}')


n = input()
sum_of_all_even_odd(n)
