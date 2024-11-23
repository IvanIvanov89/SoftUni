target_book = input()

command_or_book = input()
counter = 0

while command_or_book != 'No More Books':
    book = command_or_book
    if book == target_book:
        break
    counter += 1
    command_or_book = input()

if command_or_book == 'No More Books':
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')
else:
    print(f"You checked {counter} books and found it.")
