judges = int(input())

command = input()

all_marks = 0
total_mark_counter = 0

while command != "Finish":
    theme = command
    current_mark = 0
    for idx in range(judges):
        mark = float(input())
        all_marks += mark
        total_mark_counter += 1
        current_mark += mark

    theme_average = current_mark / judges
    print(f'{theme} - {theme_average :.2f}.')

    command = input()

print(f'Student\'s final assessment is {all_marks / total_mark_counter :.2f}.')
