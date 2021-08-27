needed_experience = float(input())
count_of_battles = int(input())
counter = 0
total = 0

for b in range(1, count_of_battles + 1):
    sum_of = 0
    experience = int(input())
    counter += 1
    if counter % 3 == 0:
        sum_of = experience * 1.15
        total += sum_of
    elif counter % 5 == 0:
        sum_of = experience * 0.1
        experience -= sum_of
        total += experience
    else:
        total += experience
    if total >= needed_experience:
        break
if total >= needed_experience:
    print(f"Player successfully collected his needed experience for {counter} battles.")
else:
    sad = needed_experience - total
    print(f"Player was not able to collect the needed experience, {sad:.2f} more needed.")

