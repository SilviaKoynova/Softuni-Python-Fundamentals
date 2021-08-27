lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
for loses in range(1, lost_fights + 1):
    if loses % 2 == 0:
        expenses += helmet_price
    if loses % 3 == 0:
        expenses += sword_price
    if loses % 6 == 0:
        expenses += shield_price
    if loses % 12 == 0:
        expenses += armor_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
