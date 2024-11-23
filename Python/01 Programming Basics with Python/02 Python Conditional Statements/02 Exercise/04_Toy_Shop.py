_Price_For_Trip = float(input())
_Puzzles_Sold = int(input())
_Dolls_Sold = int(input())
_Bears_Sold = int(input())
_Minions_Sold = int(input())
_Trucks_Sold = int(input())

_Sold_Items_Count = _Puzzles_Sold + _Dolls_Sold + _Bears_Sold + _Minions_Sold + _Trucks_Sold

_Amount_For_Sold_Items = (_Puzzles_Sold * 2.60) +\
                         (_Dolls_Sold * 3) +\
                         (_Bears_Sold * 4.10) +\
                         (_Minions_Sold * 8.20) +\
                         (_Trucks_Sold * 2)

if _Sold_Items_Count < 50:
    _Profit = _Amount_For_Sold_Items * 0.90
    if _Price_For_Trip <= _Profit:
        _Enough = _Profit - _Price_For_Trip
        print(f"Yes! {_Enough:.2f} lv left.")
    else:
        _Not_Enough = _Price_For_Trip - _Profit
        print(f"Not enough money! {_Not_Enough:.2f} lv needed.")
else:
    _Discounted_Price = _Amount_For_Sold_Items * 0.75
    _Profit = _Discounted_Price * 0.90
    if _Price_For_Trip <= _Profit:
        _Enough = _Profit - _Price_For_Trip
        print(f"Yes! {_Enough:.2f} lv left.")
    else:
        _Not_Enough = _Price_For_Trip - _Profit
        print(f"Not enough money! {_Not_Enough:.2f} lv needed.")
