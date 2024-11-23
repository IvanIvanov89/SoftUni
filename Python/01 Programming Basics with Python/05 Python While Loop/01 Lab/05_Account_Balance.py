deposit = input()

sum_in_account = 0

while deposit != 'NoMoreMoney':
    amount = float(deposit)
    if amount <= 0:
        print(f'Invalid operation!')
        break
    sum_in_account += amount
    print(f'Increase: {amount:.2f}')
    deposit = input()

print(f'Total: {sum_in_account:.2f}')
