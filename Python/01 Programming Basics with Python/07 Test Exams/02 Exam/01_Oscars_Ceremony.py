rent = int(input())

statue_price = rent * 0.70
catering_price = statue_price * 0.85
sound_price = catering_price / 2

result = statue_price + catering_price + sound_price + rent

print(f'{result :.2f}')
