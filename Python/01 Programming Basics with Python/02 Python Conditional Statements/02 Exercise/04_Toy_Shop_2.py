#count
price_excursion = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

#cena
puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

#total

total_price = (puzzles_count * puzzle_price) + \
              (dolls_count * doll_price) + \
              (bears_count * bear_price) + \
              (minions_count * minion_price) + \
              (trucks_count * truck_price)

#poruchki
total_toys = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

#otstupka
if total_toys >= 50:
    total_price *= 0.75 #za 25%

#naem
rent = total_price * 0.10
total_price_after_rent = total_price - rent


#proverka keshovica
if total_price_after_rent >= price_excursion:
    left_money = total_price_after_rent - price_excursion
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = price_excursion - total_price_after_rent
    print(f"Not enough money! {needed_money:.2f} lv needed.")