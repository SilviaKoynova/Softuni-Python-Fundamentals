def character_between(first_chr, second_chr):
    for character in range(first_chr + 1, second_chr):
        result = chr(character)
        print(result, end=" ")


character_one = ord(input())
character_two = ord(input())
character_between(character_one, character_two)
