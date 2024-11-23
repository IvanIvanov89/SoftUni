# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)

cargos = int(input())
total_weigh = 0

bus_transported = 0
truck_transported = 0
train_transported = 0

for _ in range(cargos):
    cargo_weigh = int(input())

    if cargo_weigh <= 3:
        bus_transported += cargo_weigh
    elif 4 <= cargo_weigh <= 11:
        truck_transported += cargo_weigh
    elif 12 <= cargo_weigh:
        train_transported += cargo_weigh

total_weigh = bus_transported + truck_transported + train_transported

bus_percent = (bus_transported / total_weigh) * 100
truck_percent = (truck_transported / total_weigh) * 100
train_percent = (train_transported / total_weigh) * 100
average_price = ((bus_transported * 200) + (truck_transported * 175) + (train_transported * 120)) / total_weigh

print(f'{average_price:.2f}')
print(f'{bus_percent:.2f}%')
print(f'{truck_percent:.2f}%')
print(f'{train_percent:.2f}%')
