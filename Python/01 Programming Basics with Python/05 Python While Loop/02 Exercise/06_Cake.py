cake_side_a = int(input())
cake_side_b = int(input())

cake_volume = cake_side_a * cake_side_b
pieces_taken = 0

command = input()

while command != 'STOP':
    pieces = int(command)
    pieces_taken += pieces
    if pieces_taken >= cake_volume:
        break
    command = input()

if command == 'STOP':
    pieces_left = cake_volume - pieces_taken
    print(f'{pieces_left} pieces are left.')
else:
    pieces_missing = pieces_taken - cake_volume
    print(f'No more cake left! You need {pieces_missing} pieces more.')
