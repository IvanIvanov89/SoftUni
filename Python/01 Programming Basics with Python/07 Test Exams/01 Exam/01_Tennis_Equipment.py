import math

tennis_rocket_price = float(input())
tennis_rocket_pieces = int(input())
shoes_pair_price =  tennis_rocket_price / 6
shoes_pairs = int(input())

total_for_rockets = tennis_rocket_price * tennis_rocket_pieces
total_for_shoes = shoes_pair_price * shoes_pairs
total_for_others = (total_for_rockets + total_for_shoes) / 5

grand_total = total_for_rockets + total_for_shoes + total_for_others

total_for_player = grand_total / 8
total_for_sponsors = grand_total - total_for_player

print(f'Price to be paid by Djokovic {math.floor(total_for_player)}')
print(f'Price to be paid by sponsors {math.ceil(total_for_sponsors)}')
