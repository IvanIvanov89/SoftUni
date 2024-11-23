inherited_money = float(input())
year_to_live = int(input())

starting_years = 17


for idx in range(1800, year_to_live + 1, 1):
    inherited_money = round(inherited_money, 2)
    starting_years += 1
    if idx % 2 != 0:
        inherited_money -= (12_000 + (50 * starting_years))
    else:
        inherited_money -= 12_000

if inherited_money >= 0:
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')
else:
    print(f'He will need {-inherited_money:.2f} dollars to survive.')
