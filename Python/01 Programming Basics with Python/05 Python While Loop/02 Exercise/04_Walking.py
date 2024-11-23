target = 10_000

steps_for_the_day = 0

command_or_steps = input()

while command_or_steps != 'Going home':
    steps = int(command_or_steps)
    steps_for_the_day += steps
    if steps_for_the_day > target:
        break
    command_or_steps = input()

if command_or_steps == 'Going home':
    extra_steps = int(input())
    steps_for_the_day += extra_steps

if target <= steps_for_the_day:
    extra_steps = steps_for_the_day - target
    print('Goal reached! Good job!')
    print(f'{extra_steps} steps over the goal!')
else:
    missing_steps = target - steps_for_the_day
    print(f'{abs(missing_steps)} more steps to reach goal.')
