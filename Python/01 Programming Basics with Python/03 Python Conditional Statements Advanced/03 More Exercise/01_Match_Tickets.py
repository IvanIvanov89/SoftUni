VIP_TICKET = 499.99
NORMAL_TICKET = 249.99

budget = float(input())
category_ticket = input()
number_of_people = int(input())

transport = 0.00
ticket_price = 0.00
amount_for_tickets = 0.00

if 1 <= number_of_people <= 4:
    transport = budget * 0.75

elif number_of_people <= 9:
    transport = budget * 0.60

elif number_of_people <= 24:
    transport = budget * 0.50

elif number_of_people <= 49:
    transport = budget * 0.40

else:
    transport = budget * 0.25

if category_ticket == 'VIP':
    ticket_price = 499.99
    amount_for_tickets = ticket_price * number_of_people

elif category_ticket == 'Normal':
    ticket_price = 249.99
    amount_for_tickets = ticket_price * number_of_people

budget_after_transport = budget - transport

if budget_after_transport > amount_for_tickets:
    money_left = budget_after_transport - amount_for_tickets
    print_string = f'Yes! You have {money_left:.2f} leva left.'
elif amount_for_tickets > budget_after_transport:
    money_short = amount_for_tickets - budget_after_transport
    print_string = f'Not enough money! You need {money_short:.2f} leva.'

print(print_string)
