bottles_detergent = int(input())
one_bottle = 750

for_dish = 5
for_pot = 15
dishes_to_wash = 0
pot_to_wash = 0
counter = 0
used = 0
total_detergent_start = bottles_detergent * one_bottle

command = input()

while command != 'End':
    pieces = int(command)
    counter += 1
    if counter % 3 != 0:
        dishes_to_wash += pieces
        used += pieces * for_dish
    else:
        pot_to_wash += pieces
        used += pieces * for_pot
    if used > total_detergent_start:
        break
    command = input()

if total_detergent_start >= used:
    left_over_detergent = total_detergent_start - used
    print(f'Detergent was enough!')
    print(f'{dishes_to_wash} dishes and {pot_to_wash} pots were washed.')
    print(f'Leftover detergent {left_over_detergent:} ml.')
else:
    not_enough_detergent = used - total_detergent_start
    print(f'Not enough detergent, {not_enough_detergent} ml. more necessary!')
