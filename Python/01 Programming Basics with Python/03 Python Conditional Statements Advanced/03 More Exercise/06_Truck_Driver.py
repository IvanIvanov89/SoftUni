season = input()  # Spring, Summer, Autumn, Winter
kilometers_per_month = float(input())
# Season is 4 months
price_per_km = 0
if kilometers_per_month <= 5_000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
    elif season == 'Summer':
        price_per_km = 0.90
    elif season == 'Winter':
        price_per_km = 1.05

elif 5_000 < kilometers_per_month <= 10_000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
    elif season == 'Summer':
        price_per_km = 1.10
    elif season == 'Winter':
        price_per_km = 1.25
elif 10_000 < kilometers_per_month <= 20_000:
    price_per_km = 1.45

money = 4 * (kilometers_per_month * price_per_km)
money *= 0.90

print(f'{money:.2f}')
