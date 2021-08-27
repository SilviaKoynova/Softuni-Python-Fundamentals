series_of_strings = input().split()
data = input()
while not data == 'end':
    command = data.split()[0]
    if command == 'reverse':
        startReverse = int(data.split()[2])
        countReverse = int(data.split()[4])
        end = startReverse + countReverse
        series_of_strings[startReverse:end] = reversed(series_of_strings[startReverse:end])
    elif command == 'sort':
        startSort = int(data.split()[2])
        countSort = int(data.split()[4])
        endSort = startSort + countSort
        series_of_strings[startSort:endSort] = sorted(series_of_strings[startSort:endSort])
    elif command == 'remove':
        countRemove = int(data.split()[1])
        del series_of_strings[:countRemove]

    data = input()
print(', '.join(map(str, series_of_strings)))
