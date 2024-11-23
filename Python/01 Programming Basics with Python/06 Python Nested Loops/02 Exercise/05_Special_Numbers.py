number = int(input())

for idx in range(1111, 9999 + 1,):
    idx_string = str(idx)

    special = True

    for char in idx_string:
        char = int(char)

        if char == 0:
            special = False
            break

        if number % char != 0:
            special = False
            break

    if special:
        print(idx, end= ' ')
print()
