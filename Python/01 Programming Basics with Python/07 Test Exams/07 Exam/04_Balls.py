import math

total_balls = int(input())

total_points = 0.0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls_divisions = 0

for _ in range(total_balls):
    ball = input()

    if ball == 'red':
        total_points += 5
        red_balls += 1
    elif ball == 'orange':
        total_points += 10
        orange_balls += 1
    elif ball == 'yellow':
        total_points += 15
        yellow_balls += 1
    elif ball == 'white':
        total_points += 20
        white_balls += 1
    elif ball == 'black':
        total_points = math.floor(total_points / 2)
        black_balls_divisions += 1
    else:
        other_balls += 1
        continue
print(f'Total points: {round(total_points)}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_balls_divisions}')
