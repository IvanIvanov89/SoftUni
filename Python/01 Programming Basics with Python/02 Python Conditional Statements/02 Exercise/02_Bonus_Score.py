_Number = int(input())
_Bonus = 0

if _Number <= 100:  # +5 Bonus
    _Bonus = 5
elif 100 < _Number <= 1000:  # +20%
    _Bonus = _Number * 0.2
elif 1000 < _Number:  # +10%
    _Bonus = _Number * 0.1

if _Number % 2 == 0:
    _Bonus = _Bonus + 1
elif _Number % 10 == 5:
    _Bonus = _Bonus + 2

print(_Bonus)
print(_Number + _Bonus)
