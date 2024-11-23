alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

command = input()

string = ''
bad_string = 'con'
bad_string_counter = ''
string_to_print = ''

while command != 'End':
    if command in alphabet:
    # if command.isalpha():
        letter = command

        if len(bad_string_counter) == 3:
            bad_string_counter = ''
            string_to_print = string
            string += ' '

        if letter in bad_string and letter not in bad_string_counter:
            bad_string_counter += letter

        else:
            string += letter

    command = input()

if command == 'End' and len(bad_string_counter) == 3:
    print(f'{string}')
else:
    print(string_to_print)
