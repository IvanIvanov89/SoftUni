strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price * 0.60
bananas_price = raspberry_price * 0.20

strawberry = strawberry_kg * strawberry_price
bananas = bananas_kg * bananas_price
raspberry = raspberry_kg * raspberry_price
oranges = oranges_kg * oranges_price

all_items = strawberry + bananas + raspberry + oranges


print(f'{all_items :.2f}')
