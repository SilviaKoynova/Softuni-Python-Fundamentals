line = input()
strength = 0
new_string = ""
exploding = False
for k in range(len(line)):
    if line[k] == ">":
        if line[k+1].isdigit():
            strength += int(line[k+1])
        exploding = True
        new_string += line[k]
    elif exploding:
        if line[k] == ">":
            new_string += line[k]
            if line[k+1].isdigit():
                strength += int(line[k+1])
        else:
            strength -= 1
            if strength == 0:
                exploding = False
    else:
        new_string += line[k]
print(new_string)