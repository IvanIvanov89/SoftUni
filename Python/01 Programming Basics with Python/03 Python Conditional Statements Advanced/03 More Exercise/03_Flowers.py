hrizantemi_pieces = int(input())
rose_pieces = int(input())
laleta_pieces = int(input())
season = input()  # Spring, Summer, Autumn, Winter
holiday = input()  # Y, N

total_flowers = hrizantemi_pieces + rose_pieces + laleta_pieces

if season == 'Spring' or season == 'Summer':
    hrizantemi_price = 2.00
    roses_price = 4.10
    laleta_price = 2.50
elif season == 'Autumn' or season == 'Winter':
    hrizantemi_price = 3.75
    roses_price = 4.50
    laleta_price = 4.15

if holiday == 'Y':
    hrizantemi_price *= 1.15
    roses_price *= 1.15
    laleta_price *= 1.15


total_price = hrizantemi_pieces * hrizantemi_price + rose_pieces * roses_price + laleta_pieces * laleta_price

if laleta_pieces > 7 and season == 'Spring':
    total_price *= 0.95
if  rose_pieces >= 10 and season == 'Winter':
    total_price *= 0.90
if total_flowers > 20:
    total_price *= 0.80
total_price += 2

print(f'{total_price:.2f}')
