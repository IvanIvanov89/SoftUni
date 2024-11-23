n = int(input())

first_pair_sum = 0
second_pair_sum = 0
difference = 0
maximum_difference = 0

is_Equal = True

for idx in range(n):
    if idx % 2 == 0:
        first_number = int(input())
        second_number = int(input())
        first_pair_sum = first_number + second_number
    else:
        first_number = int(input())
        second_number = int(input())
        second_pair_sum = first_number + second_number
    if idx > 0:
        difference = first_pair_sum - second_pair_sum

        if difference > maximum_difference or maximum_difference == 0:
            maximum_difference = difference
        if first_pair_sum != second_pair_sum:
            is_Equal = False

if is_Equal:
    print(f'Yes, value={first_pair_sum}')
else:
    print(f'No, maxdiff={abs(maximum_difference)}')
