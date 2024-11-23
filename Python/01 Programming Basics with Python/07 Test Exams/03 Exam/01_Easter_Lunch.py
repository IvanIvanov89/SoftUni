kozunak = int(input())
kori_s_eggs = int(input())
biscuits_kg = int(input())

kozunak_price = kozunak * 3.20
biscuits_price = biscuits_kg * 5.40
eggs_price = kori_s_eggs * 4.35 + (0.15 * (kori_s_eggs * 12))

all_price = kozunak_price + biscuits_price + eggs_price

print(f'{all_price :.2f}')
