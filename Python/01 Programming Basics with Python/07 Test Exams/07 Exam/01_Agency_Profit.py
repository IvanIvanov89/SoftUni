agency_name = input()
adult_tickets = int(input())
child_tickets = int(input())
adult_ticket_price = float(input())
service_tax = float(input())

child_ticket_price = adult_ticket_price * 0.30

adult_ticket_rev = adult_tickets * (adult_ticket_price + service_tax)
child_ticket_rev = child_tickets * (child_ticket_price + service_tax)

total_rev = adult_ticket_rev + child_ticket_rev

profit = total_rev * 0.20

print(f'The profit of your agency from {agency_name} tickets is {profit :.2f} lv.')
