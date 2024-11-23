_Figure = input()

if _Figure == "square":
    _Side = float(input())
    _Square_Area = _Side * _Side
    print(f"{_Square_Area:.3f}")
elif _Figure == "rectangle":
    _Side_A = float(input())
    _Side_B = float(input())
    _Rectangle_Area = _Side_A * _Side_B
    print(f"{_Rectangle_Area:.3f}")
elif _Figure == "circle":
    from math import pi
    _Radius = float(input())
    _Circle_Area = pi * _Radius * _Radius
    print(f"{_Circle_Area:.3f}")
elif _Figure == "triangle":
    _Side_A = float(input())
    _Side_hA = float(input())
    _Triangle_Area = (_Side_A * _Side_hA) / 2
    print(f"{_Triangle_Area:.3f}")
