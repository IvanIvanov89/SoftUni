number = int(input())

total_sum = 0

while True:
    new_number = int(input())
    total_sum += new_number

    if total_sum >= number:
        break

print(total_sum)
