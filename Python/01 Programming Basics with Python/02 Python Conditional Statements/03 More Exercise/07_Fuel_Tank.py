fuel_type = str(input())  # Diesel, Gasoline, Gas
fuel_in_tank = float(input())

if fuel_type not in ['Diesel', 'Gasoline', 'Gas']:
    print('Invalid fuel!')

elif fuel_in_tank < 25:
    print(f'Fill your tank with {fuel_type.lower()}!')

else:
    print(f"You have enough {fuel_type.lower()}.")