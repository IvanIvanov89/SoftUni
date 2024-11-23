tournaments_count = int(input())
starting_points = int(input())
won_points = 0
tournaments_won = 0

for idx in range(tournaments_count):
    stage_achieved = input()

    if stage_achieved == 'W':
        won_points += 2_000
        tournaments_won += 1
    elif stage_achieved == 'F':
        won_points += 1_200
    elif stage_achieved == 'SF':
        won_points += 720

total_points = starting_points + won_points
average_points = won_points / tournaments_count
won_percent = (tournaments_won / tournaments_count) * 100

print(f'Final points: {total_points}')
print(f'Average points: {int(average_points)}')
print(f'{won_percent :.2f}%')
