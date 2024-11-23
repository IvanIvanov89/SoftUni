import sys

min_number = sys.maxsize

while True:
    string_or_number = input()
    if string_or_number == 'Stop':
        print(min_number)
        break
    number = int(string_or_number)
    if number < min_number:
        min_number = number
