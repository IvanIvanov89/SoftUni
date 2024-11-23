distance = int(input())
day_or_night = (input())

day_taxi_price = distance * 0.79 + 0.70
day_bus_price = distance * 0.09
day_train_price = distance * 0.06

night_taxi_price = distance * 0.90 + 0.70

if distance <= 19:
    if day_or_night == 'day':
        print(f'{day_taxi_price:.2f}')
    else:
        print(f'{night_taxi_price:.2f}')
elif distance < 100:
    print(f'{day_bus_price:.2f}')
else:
    print(f'{day_train_price:.2f}')