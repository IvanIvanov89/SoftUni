command = input()
sum_prime = 0
sum_non_prime = 0
while command != 'stop':
    number = int(command)
    if number < 0:
        print(f'Number is negative.')
        command = input()
        continue
    result = all(number % i for i in range(2, number))
    if result:
        sum_prime += number
    else:
        sum_non_prime += number

    command = input()
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
