n = int(input())

left_side = 0
right_side = 0

for idx in range(2 * n):
    new_number = int(input())
    if idx < n:
        left_side += new_number
    else:
        right_side += new_number

if left_side == right_side:
    print_string = f'Yes, sum = {left_side}'
else:
    print_string = f'No, diff = {abs(left_side - right_side)}'

print(print_string)
