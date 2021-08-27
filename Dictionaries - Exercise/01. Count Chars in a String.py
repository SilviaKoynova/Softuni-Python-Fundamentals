word = input()
dictionary = {}
for i in word:
    if i != ' ':
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
for key, value in dictionary.items():
    print(f"{key} -> {value}")
