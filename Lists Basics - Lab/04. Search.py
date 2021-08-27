n = int(input())
word = input()
all_words = []
filtered_words = []
for iterations in range(n):
    new_word = input()
    all_words.append(new_word)
    if word in new_word:
        filtered_words.append(new_word)
print(all_words)
print(filtered_words)

