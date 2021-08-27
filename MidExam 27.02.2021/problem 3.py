data = input()
new_list = []
while not data == 'end':
    command = data.split()[0]
    if command == 'Chat':
        message = data.split()[1]
        new_list.append(message)
    elif command == 'Delete':
        messageToDelete = data.split()[1]
        if messageToDelete in new_list:
            new_list.remove(messageToDelete)
    elif command == 'Edit':
        messageToEdit = data.split()[1]
        editedVersion = data.split()[2]
        index = new_list.index(messageToEdit)
        new_list.remove(messageToEdit)
        new_list.insert(index, editedVersion)
    elif command == 'Pin':
        messagePin = data.split()[1]
        index = new_list.index(messagePin)
        new_list.pop(index)
        new_list.append(messagePin)
    elif command == 'Spam':
        pass




    data = input()
