minutes_for_control = int(input())
seconds_for_control = int(input())
distance = float(input())
speed_for_100_meters_seconds = int(input())

total_seconds = (minutes_for_control * 60) + seconds_for_control

slowdown_counter = distance / 120
total_slowdown = slowdown_counter * 2.5

player_time = (distance / 100) * speed_for_100_meters_seconds - total_slowdown

if player_time <= total_seconds:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {player_time :.3f}.')
else:
    short_in_time = player_time - total_seconds
    print(f'No, Marin failed! He was {short_in_time :.3f} second slower.')
