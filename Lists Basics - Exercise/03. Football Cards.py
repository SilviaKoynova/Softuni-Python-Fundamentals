cards = input().split()
team_a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
team_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
counter_team_a = 11
counter_team_b = 11
isTerminated = False
for card in cards:
    tokens = card.split('-')
    team = tokens[0]
    number = int(tokens[1])
    index = number - 1
    if team == 'A':
        if team_a[index] == 0:
            continue
        team_a[index] = 0
        counter_team_a -= 1
    else:
        if team_b[index] == 0:
            continue
        team_b[index] = 0
        counter_team_b -= 1
    if counter_team_a < 7 or counter_team_a < 7:
        isTerminated = True
        break
print(f'Team A - {counter_team_a}; Team B - {counter_team_b}')
if isTerminated:
    print("Game was terminated")
