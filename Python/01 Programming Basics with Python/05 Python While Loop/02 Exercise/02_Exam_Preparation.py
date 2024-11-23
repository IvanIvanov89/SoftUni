threshold_marks = int(input())

tasks_completed = 0
last_task = ''
bad_counter = 0
total_score = 0

while threshold_marks > bad_counter:
    command_or_input = input()

    if command_or_input == 'Enough':
        break
    mark = int(input())
    if mark <= 4:
        bad_counter += 1
    tasks_completed += 1
    total_score += mark
    last_task = command_or_input


average_score = total_score / tasks_completed

if bad_counter == threshold_marks:
    print(f'You need a break, {bad_counter} poor grades.')
else:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {tasks_completed}')
    print(f'Last problem: {last_task}')
