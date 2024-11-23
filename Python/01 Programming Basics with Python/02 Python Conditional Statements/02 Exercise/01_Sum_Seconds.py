_Time_First = int(input())
_Time_Second = int(input())
_Time_Third = int(input())

_Seconds = _Time_First + _Time_Second + _Time_Third

_Total_Minutes = _Seconds // 60
_Total_Seconds = _Seconds % 60

if _Total_Seconds < 10:
    print(f"{_Total_Minutes}:0{_Total_Seconds}")
else:
    print(f"{_Total_Minutes}:{_Total_Seconds}")
