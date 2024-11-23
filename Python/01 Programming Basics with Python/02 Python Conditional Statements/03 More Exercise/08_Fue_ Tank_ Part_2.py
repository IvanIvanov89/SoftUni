fuel_type = str(input())  # Gas, Gasoline, Diesel
liters_to_get = float(input())
club_card = str(input())  # Yes, No

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

gasoline_total = liters_to_get * gasoline_price
diesel_total = liters_to_get * diesel_price
gas_total = liters_to_get * gas_price

if club_card == 'Yes':
    gasoline_price -= 0.18
    diesel_price -= 0.12
    gas_price -= 0.08
    gasoline_total = liters_to_get * gasoline_price
    diesel_total = liters_to_get * diesel_price
    gas_total = liters_to_get * gas_price

if liters_to_get < 20:
    gasoline_total = liters_to_get * gasoline_price
    diesel_total = liters_to_get * diesel_price
    gas_total = liters_to_get * gas_price

elif 20 < liters_to_get <= 25:
    gasoline_total *= 0.92
    diesel_total *= 0.92
    gas_total *= 0.92
else:
    gasoline_total *= 0.90
    diesel_total *= 0.90
    gas_total *= 0.90

if fuel_type == 'Gasoline':
    print(f'{gasoline_total:.2f} lv.')
elif fuel_type == 'Diesel':
    print(f'{diesel_total:.2f} lv.')
else:
    print(f'{gas_total:.2f} lv.')