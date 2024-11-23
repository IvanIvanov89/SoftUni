side_a = int(input())
side_b = int(input())
side_c = int(input())

volume = side_a * side_b * side_c
packages_moved = 0

command = input()

while command != 'Done':
    packages = int(command)
    packages_moved += packages
    if packages_moved > volume:
        break
    command = input()

if command == 'Done':
    space_left = volume - packages_moved
    print(f'{space_left} Cubic meters left.')
else:
    space_needed = packages_moved - volume
    print(f'No more free space! You need {space_needed} Cubic meters more.')
