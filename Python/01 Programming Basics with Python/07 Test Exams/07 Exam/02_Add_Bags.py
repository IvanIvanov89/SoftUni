baggage_price_over_20kg = float(input())
baggage_weigh = float(input())
days_before_the_trip = int(input())
baggage_pieces = int(input())

if baggage_weigh < 10:
    baggage_price_over_20kg *= 0.20
elif 10 <= baggage_weigh <= 20:
    baggage_price_over_20kg *= 0.50

if days_before_the_trip > 30:
    baggage_price_over_20kg *= 1.10
elif 7 <= days_before_the_trip <= 30:
    baggage_price_over_20kg *= 1.15
elif 7 > days_before_the_trip:
    baggage_price_over_20kg *= 1.40

total = baggage_pieces * baggage_price_over_20kg

print(f'The total price of bags is: {total :.2f} lv. ')
