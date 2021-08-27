mine = {}

command = input()
while not command == 'stop':
    resource = command
    quantity = int(input())
    if resource not in mine:
        mine[resource] = 0
    mine[resource] += quantity
    command = input()

for resource, quantity in mine.items():
    print(f'{resource} -> {quantity}')