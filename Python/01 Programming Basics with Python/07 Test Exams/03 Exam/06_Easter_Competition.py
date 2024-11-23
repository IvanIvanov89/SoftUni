import sys

sweet_breads = int(input())

max_score = -sys.maxsize
max_points_name = ''

for idx in range(sweet_breads):
    current_score = 0
    maker_name = input()

    command = input()
    while command != 'Stop':
        current_score += int(command)
        command = input()
    print(f'{maker_name} has {current_score} points.')

    if max_score < current_score:
        max_score = current_score
        max_points_name = maker_name
        print(f'{maker_name} is the new number 1!')


print(f'{max_points_name} won competition with {max_score} points!')
