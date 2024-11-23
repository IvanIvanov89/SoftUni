from math import floor, ceil

magnoliya_pieces = int(input())
zyumbyul_pieces = int(input())
rose_pieces = int(input())
cactus_pieces = int(input())
gift_price = float(input())

magnoliya_revenue = magnoliya_pieces * 3.25
zyumbyul_revenue = zyumbyul_pieces * 4
rose_revenue = rose_pieces * 3.5
cactus_revenue = cactus_pieces * 8

total_revenue = magnoliya_revenue + zyumbyul_revenue + rose_revenue + cactus_revenue
#print(total_revenue)

total_revenue_minus_tax = total_revenue * 0.95
#print(total_revenue_minus_tax)

if total_revenue_minus_tax >= gift_price:
    total_revenue_minus_tax -= gift_price
    print(f'She is left with {floor(total_revenue_minus_tax)} leva.')

else:
    money_short = gift_price - total_revenue_minus_tax
    print(f'She will have to borrow {ceil(money_short)} leva.')