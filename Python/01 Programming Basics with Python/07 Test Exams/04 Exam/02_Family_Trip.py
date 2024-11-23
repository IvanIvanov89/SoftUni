budget = float(input())
nights_to_spend = int(input())
night_price = float(input())
extra_expense_percent = int(input())

if nights_to_spend > 7:
    night_price *= 0.95


extra_expenses = budget * (extra_expense_percent / 100)


money_for_stay = nights_to_spend * night_price

total = money_for_stay + extra_expenses

if budget >= total:
    extra_money = budget - total
    print(f'Ivanovi will be left with {extra_money :.2f} leva after vacation.')
else:
    money_short = total - budget
    print(f'{money_short :.2f} leva needed.')
