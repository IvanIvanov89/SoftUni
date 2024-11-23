import math

world_record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1_meter = float(input())


time_in_seconds_for_total_distance = distance_in_meters * time_in_seconds_for_1_meter
slowdown = math.floor(distance_in_meters / 15) * 12.5

total_time = time_in_seconds_for_total_distance + slowdown

if total_time < world_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    short = total_time - world_record_in_seconds
    print(f"No, he failed! He was {short:.2f} seconds slower.")
