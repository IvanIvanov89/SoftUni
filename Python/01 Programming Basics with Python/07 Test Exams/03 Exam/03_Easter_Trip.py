# Дестинация	    21-23 март	    24-27 март	    28-31 март
# Франция	          30 лв.	       35 лв.	       40 лв.
# Италия	          28 лв.	       32 лв.	       39 лв.
# Германия	          32 лв.	       37 лв.	       43 лв.

destination = input()  # France, Italy, Germany
reservation_date = input()  # 21-23, 24-27, 28-31
nights_to_spend = int(input())

price_for_night = 0

if destination == 'France':
    if reservation_date == '21-23':
        price_for_night = 30
    elif reservation_date == '24-27':
        price_for_night = 35
    elif reservation_date == '28-31':
        price_for_night = 40
elif destination == 'Italy':
    if reservation_date == '21-23':
        price_for_night = 28
    elif reservation_date == '24-27':
        price_for_night = 32
    elif reservation_date == '28-31':
        price_for_night = 39
elif destination == 'Germany':
    if reservation_date == '21-23':
        price_for_night = 32
    elif reservation_date == '24-27':
        price_for_night = 37
    elif reservation_date == '28-31':
        price_for_night = 43

expenses =  nights_to_spend * price_for_night
print(f'Easter trip to {destination} : {expenses :.2f} leva.')
