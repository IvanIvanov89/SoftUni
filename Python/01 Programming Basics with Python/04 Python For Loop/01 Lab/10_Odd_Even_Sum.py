n = int(input())

even_positions = 0
odd_positions = 0

for idx in range(n):
    new_number = int(input())
    if idx % 2 == 0:
        even_positions += new_number
    else:
        odd_positions += new_number

if even_positions == odd_positions:
    print_string_1 = 'Yes'
    print_string_2 = f'Sum = {even_positions}'
else:
    print_string_1 = 'No'
    print_string_2 = f'Diff = {abs(even_positions-odd_positions)}'

print(print_string_1)
print(print_string_2)
