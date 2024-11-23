days_off_per_year = int(input())

play_time_per_year = 30000  # Minutes!
year = 365  # Days!
days_on_per_year = year - days_off_per_year

play_time_on_days_on = days_on_per_year * 63
play_time_on_days_off = days_off_per_year * 127

total_play_time_per_year = play_time_on_days_on + play_time_on_days_off

if play_time_per_year <= total_play_time_per_year:
    overtime = total_play_time_per_year - play_time_per_year  # In Minutes!
    overtime_in_hours = overtime // 60
    overtime_in_minutes = overtime % 60
    print(f'Tom will run away')
    print(f'{overtime_in_hours} hours and {overtime_in_minutes} minutes more for play')

else:
    enough_time = play_time_per_year - total_play_time_per_year
    overtime_in_hours = enough_time // 60
    overtime_in_minutes = enough_time % 60
    print(f'Tom sleeps well')
    print(f'{overtime_in_hours} hours and {overtime_in_minutes} minutes less for play')