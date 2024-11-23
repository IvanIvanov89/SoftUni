#26.00 - 35.00	Hot
#20.1 - 25.9 	Warm
#15.00 - 20.00	Mild
#12.00 - 14.9	Cool
#5.00 - 11.9 	Cold

_Celsius = float(input())

if _Celsius < 0:
    print("unknown")
elif _Celsius == 0:
    print("unknown")
elif _Celsius <= 4.9 and _Celsius >= 0.1:
    print("unknown")
elif _Celsius <= 11.9 and _Celsius >= 5.00:
    print("Cold")
elif _Celsius <= 14.9 and _Celsius >= 12.00:
    print("Cool")
elif _Celsius <= 20.00 and _Celsius >= 15.00:
    print("Mild")
elif _Celsius <= 25.9 and _Celsius >= 20.1:
    print("Warm")
elif _Celsius <= 35.00 and _Celsius >= 26.00:
    print("Hot")
elif _Celsius > 35.00:
    print("unknown")
