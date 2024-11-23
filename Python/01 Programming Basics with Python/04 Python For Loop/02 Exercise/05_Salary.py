import math

open_tabs = int(input())
salary = float(input())

for _ in range(open_tabs):
    websites = input()
    if websites == 'Facebook':
        salary -= 150
        if salary <= 0:
            print(f'You have lost your salary.')
            break
    elif websites == 'Instagram':
        salary -= 100
        if salary <= 0:
            print(f'You have lost your salary.')
            break
    elif websites == 'Reddit':
        salary -= 50
        if salary <= 0:
            print(f'You have lost your salary.')
            break
if salary > 0:
    print(math.floor(salary))
