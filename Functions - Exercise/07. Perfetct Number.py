def perfect_num(number):
    sum_of_numbers = 0
    for num in range(1, number):
        if number % num == 0:
            sum_of_numbers += num

    if sum_of_numbers == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


n = int(input())
perfect_num(n)
