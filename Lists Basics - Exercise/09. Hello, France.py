items_with_their_prices = input().split('|')
budget = float(input())
bought_items = []
profit = 0
for item in items_with_their_prices:
    type_of_item, item_price = item.split('->')
    item_price = float(item_price)
    if type_of_item == 'Clothes' and item_price > 50:
        continue
    elif type_of_item == 'Shoes' and item_price > 35:
        continue
    elif type_of_item == 'Accessories' and item_price > 20.50:
        continue
    if budget >= item_price:
        budget -= item_price
        current_profit = item_price * 0.40
        profit += current_profit
        bought_items.append(item_price+current_profit)
for el in bought_items:
    print(f"{el:.2f}", end=' ')

print()
print(f"Profit: {profit:.2f}")
budget += sum(bought_items)
if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
