target_height = int(input())

starting_height = target_height - 30

is_goal = False

jump_height = 0
jump_counter = 0
print_string = ''

while not is_goal:

    for idx in range(1, 3 + 1):
        jump_height = int(input())
        jump_counter += 1

        if jump_height > starting_height:
            if starting_height >= target_height:
                print_string = f'Tihomir succeeded, he jumped over {target_height}cm after {jump_counter} jumps.'
                is_goal = True
                break
            starting_height += 5
            break
        if idx == 3 and jump_height <= starting_height:
            print_string = f'Tihomir failed at {starting_height}cm after {jump_counter} jumps.'
            is_goal = True
            break
    continue

print(print_string)
