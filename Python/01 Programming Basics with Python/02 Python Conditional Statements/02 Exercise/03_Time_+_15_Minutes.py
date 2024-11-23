_Hour = int(input())
_Minutes = int(input())
_15_Minutes = 15

_Hour_To_Minutes = _Hour * 60
_Total_Minutes = _Hour_To_Minutes + _Minutes + _15_Minutes

_For_Hour = _Total_Minutes // 60
_For_Minutes = _Total_Minutes % 60

if _For_Hour == 24 and _For_Minutes < 10:
    print(f"0:0{_For_Minutes}")

elif _For_Minutes < 10:
    print(f"{_For_Hour}:0{_For_Minutes}")

elif _For_Hour == 24:
    print(f"0:{_For_Minutes}")

else:
    print(f"{_For_Hour}:{_For_Minutes}")
