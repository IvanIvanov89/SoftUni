guests = int(input())
price_for_one_guest = float(input())
budget = float(input())

cake_price = budget * 0.10

if 10 <= guests <= 15:
    price_for_one_guest *= 0.85
elif 16 <= guests <= 20:
    price_for_one_guest *= 0.80
elif 21 <= guests:
    price_for_one_guest *= 0.75

price_for_all = (price_for_one_guest * guests) + cake_price

if budget >= price_for_all:
    money_left = budget - price_for_all
    print(f'It is party time! {money_left :.2f} leva left.')
else:
    money_needed = price_for_all - budget
    print(f'No party! {money_needed :.2f} leva needed.')
