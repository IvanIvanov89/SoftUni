hour = int(input())
day_of_the_week = input()

state = ''

if (day_of_the_week == 'Monday'
        or day_of_the_week == 'Tuesday'
        or day_of_the_week == 'Wednesday'
        or day_of_the_week == 'Thursday'
        or day_of_the_week == 'Friday'
        or day_of_the_week == 'Saturday'):
    if 10 <= hour <= 18:
        state = 'open'
    else:
        state = 'closed'
else:
    state = 'closed'

print(state)