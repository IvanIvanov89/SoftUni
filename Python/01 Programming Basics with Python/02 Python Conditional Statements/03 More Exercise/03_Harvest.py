import math

field_square_meters = int(input())
grapes_per_square_meter = float(input())
wine_needed = int(input())
workers = int(input())

total_grapes = grapes_per_square_meter * field_square_meters  # 100% от реколтата!

grapes_for_wine = total_grapes * 0.40  # 40% от реколтата!

wine_produced = grapes_for_wine / 2.5  # В литри!

if wine_produced >= wine_needed:
    wine_left = wine_produced - wine_needed
    wine_per_worker = wine_left / workers
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_worker)} liters per person.')
else:
    wine_short = wine_needed - wine_produced
    print(f'It will be a tough winter! More {math.floor(wine_short)} liters wine needed.')