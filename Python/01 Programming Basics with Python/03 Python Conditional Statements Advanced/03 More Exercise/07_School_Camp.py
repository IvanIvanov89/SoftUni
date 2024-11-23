season = input()  # Winter, Spring, Summer
type_of_group = input()  # boys, girls, mixed
students = int(input())
nights_to_spend = int(input())

price_per_student = 0
price_for_hotel = 0
sport = ''

if type_of_group == 'boys' or type_of_group == 'girls':
    if season == 'Winter':
        price_per_student = 9.60
    elif season == 'Spring':
        price_per_student = 7.20
    elif season == 'Summer':
        price_per_student = 15
elif type_of_group == 'mixed':
    if season == 'Winter':
        price_per_student = 10
    elif season == 'Spring':
        price_per_student = 9.50
    elif season == 'Summer':
        price_per_student = 20

price_for_hotel = (students * price_per_student) * nights_to_spend

if 10 <= students < 20:
    price_for_hotel *= 0.95
elif 20 <= students < 50:
    price_for_hotel *= 0.85
elif 50 <= students:
    price_for_hotel *= 0.50

if type_of_group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'
elif type_of_group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'
elif type_of_group == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'
print(f'{sport} {price_for_hotel:.2f} lv.')
