
player_name = input()

score = 301
successful_shots = 0
unsuccessful_shots = 0
command = input()

while command != 'Retire':
    field = command  # Single, Double, Triple
    points = int(input())

    if field == 'Double':
        points *= 2
    elif field == 'Triple':
        points *= 3
    score -= points
    if score >= 0:
        successful_shots += 1
    if score < 0:
        unsuccessful_shots += 1
        score += points

    if score == 0:
        print(f'{player_name} won the leg with {successful_shots} shots.')
        break
    command = input()

if command == 'Retire' and (score > 0):
    print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
