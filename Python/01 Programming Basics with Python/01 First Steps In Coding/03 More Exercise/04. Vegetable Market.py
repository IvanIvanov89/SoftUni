_Veggies_Price = float(input())
_Fruit_Price = float(input())
_Veggie_Total_Kilos = int(input())
_Fruit_Total_Kilos = int(input())
_1Euro = 1.94
_Amount_For_Veggies = _Veggies_Price * _Veggie_Total_Kilos
_Amount_For_Fruit = _Fruit_Price * _Fruit_Total_Kilos
_Total_Amount = _Amount_For_Veggies + _Amount_For_Fruit
_Total_Amount_Euro = _Total_Amount / _1Euro
print(f"{_Total_Amount_Euro:.2f}")
