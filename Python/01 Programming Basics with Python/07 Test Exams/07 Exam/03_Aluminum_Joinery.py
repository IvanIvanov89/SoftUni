ordered_pieces = int(input())
ordered_type = input()  # 90X130, 100X150, 130X180, 200X300
delivery_type = input()  # With delivery, Without delivery

piece_price = 0.0

if ordered_type == '90X130':
    piece_price = 110
    if ordered_pieces > 60:
        piece_price *= 0.92
    elif ordered_pieces > 30:
        piece_price *= 0.95
elif ordered_type == '100X150':
    piece_price = 140
    if ordered_pieces > 80:
        piece_price *= 0.90
    elif ordered_pieces > 40:
        piece_price *= 0.94
elif ordered_type == '130X180':
    piece_price = 190
    if ordered_pieces > 50:
        piece_price *= 0.88
    elif ordered_pieces >20:
        piece_price *= 0.93
elif ordered_type == '200X300':
    piece_price = 250
    if ordered_pieces > 50:
        piece_price *= 0.86
    elif ordered_pieces > 25:
        piece_price *= 0.91

total = ordered_pieces * piece_price
if delivery_type == 'With delivery':
    total += 60

if ordered_pieces < 10:
    print(f'Invalid order')
elif 10 <= ordered_pieces <= 99:
    print(f'{total :.2f} BGN')
else:
    print(f'{total * 0.96 :.2f} BGN')
