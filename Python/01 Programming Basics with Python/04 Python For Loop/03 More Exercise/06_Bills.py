months = int(input())

electricity_bill = 0
watter_bill = 0
internet_bill = 0

for _ in range(months):
    electricity = float(input())
    electricity_bill += electricity
    watter_bill += 20
    internet_bill += 15

others_bill = (electricity_bill + watter_bill + internet_bill) * 1.20
average_bill = (electricity_bill + watter_bill + internet_bill + others_bill) / months


# •	1ви ред: "Electricity: {ток за всички месеци} lv"
print(f'Electricity: {electricity_bill:.2f} lv')
# •	2ри ред: "Water: {вода за всички месеци} lv"
print(f'Water: {watter_bill:.2f} lv')
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
print(f'Internet: {internet_bill:.2f} lv')
# •	4ти ред: "Other: {други за всички месеци} lv"
print(f'Other: {others_bill:.2f} lv')
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
print(f'Average: {average_bill:.2f} lv')
