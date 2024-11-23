expected_sum = int(input())
counter = 0
cash_payments = 0
cash_payment_counter = 0
card_payments = 0
card_payment_counter = 0
sum_gained = 0

command = input()

while command != 'End':
    donation = int(command)
    counter += 1
    if counter % 2 != 0:
        if donation > 100:
           print(f'Error in transaction!')
        else:
            cash_payments += donation
            cash_payment_counter += 1
            sum_gained += donation
            print(f'Product sold!')
    else:
        if donation < 10:
            print(f'Error in transaction!')
        else:
            card_payments += donation
            card_payment_counter += 1
            sum_gained += donation
            print(f'Product sold!')
    if sum_gained >= expected_sum:
        print(f'Average CS: {cash_payments / cash_payment_counter:.2f}')
        print(f'Average CC: {card_payments / card_payment_counter:.2f}')
        break
    else:
        command = input()
if command == "End":
    print(f'Failed to collect required money for charity.')
