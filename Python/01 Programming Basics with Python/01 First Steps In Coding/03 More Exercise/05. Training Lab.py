_W_Of_Hall = float(input()) #In Meters!!!
_H_Of_Hall = float(input()) #In Meters!!!
_1Meter = 100
# 1 Work Place =  H = 70 x W = 120 cm
# 1 Door =      - 1 Work Place
# 1 Podium =    - 2 Work Place
_W_Of_Hall_In_Centimeters = _W_Of_Hall * _1Meter
#print(_W_Of_Hall_In_Centimeters)
_H_Of_Hall_In_Centimeters = _H_Of_Hall * _1Meter
#print(_H_Of_Hall_In_Centimeters)
_H_Of_Hall_In_Centimeters_Minus_Coridor = _H_Of_Hall_In_Centimeters - _1Meter
_Max_Places_By_H = _H_Of_Hall_In_Centimeters_Minus_Coridor // 70
#print(_Max_Places_By_H)
_Max_Places_By_W = _W_Of_Hall_In_Centimeters // 120
#print(_Max_Places_By_W)
_Total_Max_Places = (_Max_Places_By_W * _Max_Places_By_H) - 3
print(f"{_Total_Max_Places:.0f}")
