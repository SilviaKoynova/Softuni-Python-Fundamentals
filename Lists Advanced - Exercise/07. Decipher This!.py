message = input().split(" ")
final_list = []
for text in message:
    digits = []
    letters = []
    for letter in text:
        if letter.isdigit():
            digits.append(letter)
        else:
            letters.append(letter)
    number = "".join(digits)
    character = int(number)
    letters[0], letters[-1] = letters[-1], letters[0]
    letters.insert(0, chr(character))
    final = "".join(letters)
    final_list.append(final)
print(" ".join(final_list))
