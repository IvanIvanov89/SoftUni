tournament_stage = input()  # Quarter final, Semi final, Final
ticket_type = input()  # Standard, Premium, VIP
tickets = int(input())
picture = input()  # Y, N
ticket_price = 0
price_for_picture = 40
if tournament_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == 'Premium':
        ticket_price = 105.20
    elif ticket_type == 'VIP':
        ticket_price = 118.90
elif tournament_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.40
elif tournament_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400
total_price = ticket_price * tickets
if total_price > 4_000:
    total_price *= 0.75
    if picture == 'Y':
        price_for_picture = 0
elif 2500 < total_price <= 4_000:
    total_price *= 0.90
if picture == 'N':
    price_for_picture = 0

final_price = total_price + price_for_picture * tickets

print(f'{final_price :.2f}')
