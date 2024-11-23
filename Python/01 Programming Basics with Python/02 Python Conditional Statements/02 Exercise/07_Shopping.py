budget = float(input())
gpu_pieces = int(input())
cpu_pieces = int(input())
ram_pieces = int(input())

price_for_gpu = 250
amount_for_gpu = gpu_pieces * price_for_gpu

price_for_cpu = amount_for_gpu * 0.35
price_for_ram = amount_for_gpu * 0.10

amount_for_cpu = cpu_pieces * price_for_cpu
amount_for_ram = ram_pieces * price_for_ram

total_price = amount_for_gpu + amount_for_cpu + amount_for_ram

if gpu_pieces > cpu_pieces:
    total_price *= 0.85

if budget >= total_price:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_short = total_price - budget
    print(f'Not enough money! You need {money_short:.2f} leva more!')