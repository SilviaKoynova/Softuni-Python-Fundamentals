message = input()
data = input()
while not data == 'End':
    split_data = data.split()
    command = split_data[0]
    if command == 'Translate':
        char = split_data[1]
        replacement = split_data[2]
        message = message.replace(char, replacement)
        print(message)
    elif command == 'Includes':
        string = split_data[1]
        if string in message:
            print('True')
        else:
            print('False')
    elif command == 'Start':
        string1 = split_data[1]
        if message.startswith(string1):
            print('True')
        else:
            print('False')
    elif command == 'Lowercase':
        message = message.lower()
        print(message)
    elif command == 'FindIndex':
        ch = split_data[1]
        index = message.rfind(ch)
        print(index)
    elif command == 'Remove':
        start_index = int(split_data[1])
        count = int(split_data[2])
        part_one = message[:start_index]
        part_two = message[start_index + count:]
        message = part_one + part_two
        print(message)

    data = input()
