books = input().split('&')
data = input()
is_valid = True
while not data == 'Done':
    instructions = data.split(' | ')
    command = instructions[0]
    if command == 'Add Book':
        name = instructions[1]
        if name not in books:
            books.insert(0, name)
    elif command == 'Take Book':
        book_name = instructions[1]
        if book_name in books:
            books.remove(book_name)
    elif command == 'Swap Books':
        name1 = instructions[1]
        name2 = instructions[2]
        if name1 in books and name2 in books:
            book1 = books.index(name1)
            book2 = books.index(name2)
            books[book1], books[book2] = books[book2], books[book1]
    elif command == 'Insert Book':
        bookName = instructions[1]
        books.append(bookName)
    elif command == 'Check Book':
        indexBook = int(instructions[1])
        if indexBook in range(len(books)):
            print(books[indexBook])

    data = input()
print(', '.join(map(str, books)))
