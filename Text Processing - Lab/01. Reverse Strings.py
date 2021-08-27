data = input()
while not data == 'end':
    command = data
    reversed_word = ''.join(reversed(command))
    print(f"{data} = {reversed_word}")
    data = input()

    
