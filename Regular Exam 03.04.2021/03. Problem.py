guests = {}
data = input()
count = 0
while not data == 'Stop':
    split_data = data.split('-')
    command = split_data[0]
    if command == 'Like':
        guest = split_data[1]
        meal = split_data[2]
        if guest in guests:
            if meal not in guests[guest]:
                guests[guest].append(meal)
        else:
            guests[guest] = []
            guests[guest].append(meal)
    elif command == 'Unlike':
        guest1 = split_data[1]
        meal1 = split_data[2]
        if guest1 in guests:
            if meal1 not in guests[guest1]:
                print(f"{guest1} doesn't have the {meal1} in his/her collection.")
            else:
                count += 1
                guests[guest1].remove(meal1)
                print(f"{guest1} doesn't like the {meal1}.")
        else:
            print(f"{guest1} is not at the party.")
    data = input()
sorted_guests = sorted(guests.items(), key=lambda x: (-len(x[1]), x[0]))
for guest, meal in sorted_guests:
    print(f"{guest}: {', '.join(meal)}")
print(f"Unliked meals: {count}")
