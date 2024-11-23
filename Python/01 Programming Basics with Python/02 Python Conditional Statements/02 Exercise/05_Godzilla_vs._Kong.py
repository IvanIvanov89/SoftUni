_Budget = float(input())
_Statists = int(input())
_Price_For_1_Statist = float(input())

_Decor = _Budget * 0.10
_Price_For_All_Statists = _Statists * _Price_For_1_Statist

if _Statists > 150:
    _Price_For_All_Statists = _Price_For_All_Statists * 0.90

_Total_Price_For_All = _Decor + _Price_For_All_Statists

if _Total_Price_For_All > _Budget:
    print("Not enough money!")
    _Not_Enough = _Total_Price_For_All - _Budget
    print(f"Wingard needs {_Not_Enough:.2f} leva more.")
else:
    print("Action!")
    _Enough = _Budget - _Total_Price_For_All
    print(f"Wingard starts filming with {_Enough:.2f} leva left.")
