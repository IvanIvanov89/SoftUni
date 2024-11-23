eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
color = ''
for idx in range(eggs):
    color = input()  # red, orange, blue, green
    if color == 'red':
        red_eggs += 1
    elif color == 'orange':
        orange_eggs += 1
    elif color == 'blue':
        blue_eggs += 1
    elif color == 'green':
        green_eggs += 1

max_value = max(red_eggs, orange_eggs, blue_eggs, green_eggs)

if max_value == red_eggs:
    color = 'red'
elif max_value == orange_eggs:
    color = 'orange'
elif max_value == blue_eggs:
    color = 'blue'
elif max_value == green_eggs:
    color = 'green'

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_value} -> {color}')
