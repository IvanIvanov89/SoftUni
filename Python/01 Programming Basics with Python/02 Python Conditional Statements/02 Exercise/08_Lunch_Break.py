import math

tv_series_name = input()
time_for_episode = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
time_for_nap = time_for_break / 4

total_time_needed = time_for_episode + time_for_lunch + time_for_nap

if time_for_break >= total_time_needed:
    time_left = time_for_break - total_time_needed
    print(f'You have enough time to watch {tv_series_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    time_short = total_time_needed - time_for_break
    print(f"You don't have enough time to watch {tv_series_name}, you need {math.ceil(time_short)} more minutes.")