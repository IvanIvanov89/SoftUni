budget = float(input())
season = input()

accommodation_type = ''
location = ''
price = 0

if budget <= 1_000:
    accommodation_type = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1_000 < budget <= 3_000:
    accommodation_type = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3_000:
    accommodation_type = 'Hotel'
    price = budget * 0.90
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

print(f'{location} - {accommodation_type} - {price:.2f}')
