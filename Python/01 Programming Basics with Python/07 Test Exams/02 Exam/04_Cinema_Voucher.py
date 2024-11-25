vaulter = int(input())

vaulter_left = vaulter

tickets_bought = 0
others_bought = 0

command = input()

while command != 'End':
    to_buy = command
    if len(to_buy) > 8:
        price = ord(to_buy[0]) + ord(to_buy[1])
        if price <= vaulter_left:
            tickets_bought += 1
    else:
        price = ord(to_buy[0])
        if price <= vaulter_left:
            others_bought += 1
    vaulter_left -= price
    if vaulter_left < 0:
        break
    command = input()

print(tickets_bought)
print(others_bought)
