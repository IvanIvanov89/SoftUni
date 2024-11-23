import sys

n = int(input())

sum_numbers = 0
max_number = -sys.maxsize

for idx in range(n):
    new_number = int(input())

    if new_number > max_number:
        max_number = new_number

    sum_numbers += new_number

if max_number == sum_numbers - max_number:
    print_string_1 = f'Yes'
    print_string_2 = f'Sum = {max_number}'
else:
    sum_numbers = sum_numbers - max_number
    print_string_1 = 'No'
    print_string_2 = f'Diff = {abs(max_number - sum_numbers)}'

print(print_string_1)
print(print_string_2)
