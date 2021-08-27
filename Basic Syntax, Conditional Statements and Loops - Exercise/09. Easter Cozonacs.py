budget = float(input())
flour_price = float(input())
cozunacs_made = 0
colored_eggs = 0
eggs_pack_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price = milk_price_per_liter / 4
cozunac_price = flour_price + eggs_pack_price + milk_price
while budget >= cozunac_price:
    cozunacs_made += 1
    colored_eggs += 3
    if cozunacs_made % 3 == 0:
        colored_eggs -= cozunacs_made - 2
    budget -= cozunac_price
print(f'You made {cozunacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
