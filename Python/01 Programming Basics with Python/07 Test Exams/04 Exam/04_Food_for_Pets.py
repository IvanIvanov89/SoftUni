days = int(input())
total_food = float(input())

dog_food_eaten = 0
cat_food_eaten = 0
biscuits_eaten = 0

for idx in range(1, days + 1):
    food_for_dog = int(input())
    dog_food_eaten += food_for_dog
    food_for_cat = int(input())
    cat_food_eaten += food_for_cat
    if idx % 3 == 0:
        food_for_the_day = food_for_dog + food_for_cat
        biscuits_eaten += food_for_the_day * 0.10

eaten_food = dog_food_eaten + cat_food_eaten
percent_eaten_food = (eaten_food / total_food) * 100
dog_percent = (dog_food_eaten / eaten_food) * 100
cat_percent = (cat_food_eaten / eaten_food) * 100

print(f'Total eaten biscuits: {int(biscuits_eaten)}gr.')
print(f'{percent_eaten_food :.2f}% of the food has been eaten.')
print(f'{dog_percent :.2f}% eaten from the dog.')
print(f'{cat_percent :.2f}% eaten from the cat.')
