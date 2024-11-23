junior_participants = int(input())
senior_participants = int(input())
trail = input()

tax_for_juniors = 0
tax_for_seniors = 0
total_participants = junior_participants + senior_participants

if trail == 'trail':
    tax_for_juniors = junior_participants * 5.50
    tax_for_seniors = senior_participants * 7
elif trail == 'cross-country':
    tax_for_juniors = junior_participants * 8
    tax_for_seniors = senior_participants * 9.50
elif trail == 'downhill':
    tax_for_juniors = junior_participants * 12.25
    tax_for_seniors = senior_participants * 13.75
elif trail == 'road':
    tax_for_juniors = junior_participants * 20
    tax_for_seniors = senior_participants * 21.50

total_tax = tax_for_juniors + tax_for_seniors

if total_participants >= 50 and trail == 'cross-country':
    total_tax *= 0.75

expenses = total_tax * 0.05
sum_gained = total_tax - expenses

print(f'{sum_gained:.2f}')
