tournaments_count = int(input())
starting_points = int(input())

bonus_points = 0
tournaments_won = 0

for _ in range(tournaments_count):
    level_reached = input()
    if level_reached == 'W':
        bonus_points += 2_000
        tournaments_won += 1
    elif level_reached == 'F':
        bonus_points += 1_200
    elif level_reached == 'SF':
        bonus_points += 720

total_points = starting_points + bonus_points

print(f'Final points: {int(total_points)}')
print(f'Average points: {int(bonus_points / tournaments_count)}')
print(f'{(tournaments_won / tournaments_count) * 100:.2f}%')
