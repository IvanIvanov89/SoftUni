import math

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day_in_grams = float(input())  # В Грамове!
turtle_food_per_day_in_grams /= 1000

dog_eats = days * dog_food_per_day
cat_eats = days * cat_food_per_day
turtle_eats = days * turtle_food_per_day_in_grams

total_food_eaten = dog_eats + cat_eats + turtle_eats

if food_left >= total_food_eaten:
    leftover = food_left - total_food_eaten
    print(f'{math.floor(leftover)} kilos of food left.')
else:
    needed = total_food_eaten - food_left
    print(f'{math.ceil(needed)} more kilos of food are needed.')