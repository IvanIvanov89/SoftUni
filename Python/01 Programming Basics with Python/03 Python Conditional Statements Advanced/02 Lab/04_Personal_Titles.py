age = float(input())
gender = input()
call = ''

if gender == 'm':
    if age >= 16:
        call = 'Mr.'
    elif age < 16:
        call = 'Master'
elif gender == 'f':
    if age >= 16:
        call = 'Ms.'
    elif age < 16:
        call = 'Miss'
print(call)