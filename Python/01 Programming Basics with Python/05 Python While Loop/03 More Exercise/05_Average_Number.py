n = int(input())

total = 0

for idx in range(n):
    new_number = int(input())
    total += new_number

print(f'{total / n:.2f}')
