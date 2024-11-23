budget = float(input())
statists = int(input())
clothing_for_one = float(input())

decor = budget * 0.10

if statists > 150:
    clothing_for_one *= 0.90

total_clothing = statists * clothing_for_one
total_expenses = total_clothing + decor

if total_expenses > budget:
    money_short = total_expenses - budget
    print(f'Not enough money!')
    print(f'Wingard needs {money_short :.2f} leva more.')

else:
    money_more = budget - total_expenses
    print(f'Action!')
    print(f'Wingard starts filming with {money_more :.2f} leva left.')
