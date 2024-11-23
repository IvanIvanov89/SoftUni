import sys

max_number = -sys.maxsize

while True:
    string_or_number = input()
    if string_or_number == 'Stop':
        print(max_number)
        break
    number = int(string_or_number)
    if number > max_number:
        max_number = number
