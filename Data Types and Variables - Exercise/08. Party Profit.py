party_size = int(input())
days = int(input())
coins = 0

for all_days in range(1, days + 1):
    if all_days % 10 == 0:
        party_size -= 2
    if all_days % 15 == 0:
        party_size += 5
        coins -= 2 * party_size
    coins += 50 - (2 * party_size)
    if all_days % 3 == 0:
        coins -= 3 * party_size
    if all_days % 5 == 0:
        coins += 20 * party_size
print(f"{party_size} companions received {coins // party_size} coins each.")
