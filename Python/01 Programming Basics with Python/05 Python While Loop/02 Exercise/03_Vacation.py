needed_money = float(input())
available_money = float(input())

days_counter = 0
money_spent_days = 0

while needed_money > available_money and money_spent_days < 5:
    operation = input()
    amount = float(input())
    days_counter += 1

    if operation == 'save':
        available_money += amount
        money_spent_days = 0
    elif operation == 'spend':
        available_money -= amount
        money_spent_days += 1
        if available_money <= 0:
            available_money = 0

if money_spent_days == 5:
    print('You can\'t save the money.')
    print(f'{days_counter}')
else:
    print(f'You saved the money for {days_counter} days.')
