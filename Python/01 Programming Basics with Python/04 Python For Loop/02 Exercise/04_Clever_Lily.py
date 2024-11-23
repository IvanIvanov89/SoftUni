age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_saved = 0
multiplier = 0
toys_collected = 0

for idx in range(1, age + 1):
    if idx % 2 == 0:
        if idx == 2:
            multiplier += 1
            money_saved += 10
        else:
            multiplier += 1
            money_saved += 10 + (10 * (multiplier - 1))
    else:
        toys_collected += 1

money_saved = money_saved - multiplier + (toys_collected * toy_price)

if money_saved >= washing_machine_price:
    print_string = f'Yes! {money_saved - washing_machine_price :.2f}'
else:
    print_string = f'No! {washing_machine_price - money_saved :.2f}'

print(print_string)
