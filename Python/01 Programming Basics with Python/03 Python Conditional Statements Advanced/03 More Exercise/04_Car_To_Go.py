budget = float(input())
season = input()
car_class = ''
car = ''
car_price = 0

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.35
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.65
elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        car = 'Cabrio'
        car_price = budget * 0.45
    elif season == 'Winter':
        car = 'Jeep'
        car_price = budget * 0.80
else:
        car_class = 'Luxury class'
        car = 'Jeep'
        car_price = budget * 0.90

print(f'{car_class}')
print(f'{car} - {car_price:.2f}')
