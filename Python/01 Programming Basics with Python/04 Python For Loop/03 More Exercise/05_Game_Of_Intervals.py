number_of_moves = int(input())
result = 0
interval_to_9 = 0
interval_to_19 = 0
interval_to_29 = 0
interval_to_39 = 0
interval_to_50 = 0
interval_invalid = 0
for _ in range(number_of_moves):
    new_number = int(input())
# •	От 0 до 9  20 % от числото
    if 0 <= new_number <= 9:
        interval_to_9 += 1
        result += new_number * 0.20
# •	От 10 до 19  30 % от числото
    elif 0 <= new_number <= 19:
        interval_to_19 += 1
        result += new_number * 0.30
# •	От 20 до 29  40 % от числото
    elif 0 <= new_number <= 29:
        interval_to_29 += 1
        result += new_number * 0.40
# •	От 30 до 39  50 точки
    elif 0 <= new_number <= 39:
        interval_to_39 += 1
        result += 50
# •	От 40 до 50  100 точки
    elif 0 <= new_number <= 50:
        interval_to_50 += 1
        result += 100
    else:
        interval_invalid += 1
        result /= 2

print(f'{result:.2f}')
print(f'From 0 to 9: {interval_to_9 / number_of_moves * 100:.2f}%')
print(f'From 10 to 19: {interval_to_19 / number_of_moves * 100:.2f}%')
print(f'From 20 to 29: {interval_to_29 / number_of_moves * 100:.2f}%')
print(f'From 30 to 39: {interval_to_39 / number_of_moves * 100:.2f}%')
print(f'From 40 to 50: {interval_to_50 / number_of_moves * 100:.2f}%')
print(f'Invalid numbers: {interval_invalid / number_of_moves * 100:.2f}%')
