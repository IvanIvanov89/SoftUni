import math
from math import ceil
#	Паламуд – 60% по-скъп от скумрията
#	Сафрид – 80% по-скъп от цацата
#	Миди – 7.50 лв. за килограм
#Oт конзолата се въвеждат цените в лева на скумрията и цацата. Също количеството на паламуд,
# сафрид и миди в килограми.
# Да се отпечата на конзолата едно число с плаваща запетая: колко пари ще са нужни на Георги, за да си плати сметката.
# Числото трябва да е форматирано до вторият знак след десетичната запетая (1.2457 -> 1.25).

_Midi_Price = 7.50

_Price_For_KG_Skumria = float(input())
_Price_For_KG_Caca = float(input())

_KG_Bought_Palamud = float(input())
_KG_Bought_Safrid = float(input())
_KG_Bought_Midi = int(input())

_Price_For_Palamud = (_Price_For_KG_Skumria + (0.60 * _Price_For_KG_Skumria))
#print(_Price_For_Palamud)

_Price_For_Safrid = (_Price_For_KG_Caca + (0.80 * _Price_For_KG_Caca))
#print(_Price_For_Safrid)

_Amount_For_Pamamud = _KG_Bought_Palamud * _Price_For_Palamud
#print(_Amount_For_Pamamud)
_Amount_For_Safrid =  _KG_Bought_Safrid * _Price_For_Safrid
#print(_Amount_For_Safrid)
_Amount_For_Midi = _KG_Bought_Midi * _Midi_Price
#print(_Amount_For_Midi)

_Total_Amount = _Amount_For_Midi + _Amount_For_Safrid + _Amount_For_Pamamud
print(f"{_Total_Amount:.2f}")
