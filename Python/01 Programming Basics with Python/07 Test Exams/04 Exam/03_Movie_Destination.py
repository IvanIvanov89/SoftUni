budget = float(input())
destination = input()  # Dubai, Sofia, London
season = input()  # Summer, Winter
days = int(input())

price_for_a_day = 0

if season == 'Winter':
    if destination == 'Dubai':
        price_for_a_day += 45_000
    elif destination == 'Sofia':
        price_for_a_day += 17_000
    elif destination == 'London':
        price_for_a_day += 24_000
elif season == 'Summer':
    if destination == 'Dubai':
        price_for_a_day += 40_000
    elif destination == 'Sofia':
        price_for_a_day += 12_500
    elif destination == 'London':
        price_for_a_day += 20_250

total_price = days * price_for_a_day

if destination == 'Dubai':
    total_price *= 0.70
elif destination == 'Sofia':
    total_price *= 1.25

if budget >= total_price:
    extra_money = budget - total_price
    print(f'The budget for the movie is enough! We have {extra_money :.2f} leva left!')
else:
    money_short = total_price - budget
    print(f'The director needs {money_short :.2f} leva more!')
