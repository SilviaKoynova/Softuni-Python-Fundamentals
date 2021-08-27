def total_price(product, q):
    if product == 'coffee':
        return 1.50 * q
    elif product == 'water':
        return 1.00 * q
    elif product == 'coke':
        return 1.40 * q
    elif product == 'snacks':
        return 2.00 * q


first_product = input()

quantity = int(input())
result = total_price(first_product, quantity)
print(f'{result:.2f}')
