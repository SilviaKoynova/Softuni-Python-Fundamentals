gifts = input().split()
data = input()
while not data == 'No Money':
    command = data.split()[0]
    if command == 'OutOfStock':
        gift = data.split()[1]
        newGift = 'None'
        if gift in gifts:
            for i in gifts:
                if i == gift:
                    pos = gifts.index(gift)
                    gifts.insert(pos, newGift)
                    gifts.remove(gift)
    elif command == 'Required':
        gift1 = data.split()[1]
        index1 = int(data.split()[2])
        if index1 in range(len(gifts)):
            gifts.insert(index1, gift1)
            odd = index1 + 1
            gifts.pop(odd)
    elif command == 'JustInCase':
        finalGift = data.split()[1]
        gifts.append(finalGift)
        gifts.pop(-2)

    data = input()
sorted_gifts = [gif for gif in gifts if not gif == 'None']
print(*sorted_gifts)
