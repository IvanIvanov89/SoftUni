# Steni = Green
# Pokriv = Red
_x = float(input())
_y = float(input())
_h = float(input())
# Walls
_H_Of_Walls = _x - _h

_Walls_Front_Back = (_x * _x) * 2
_Front_Door = 1.2 * 2
_Area_Walls_Fron_Back = _Walls_Front_Back - _Front_Door
#print(_Area_Walls_Fron_Back)

_Walls_Left_Right = (_x * _y) * 2
_Windows_On_Both_Sides = (1.5 * 1.5) * 2
_Area_Walls_Left_Right = _Walls_Left_Right - _Windows_On_Both_Sides
#print(_Area_Walls_Left_Right)

_Total_Area_Of_Walls = _Area_Walls_Fron_Back + _Area_Walls_Left_Right
#print(_Total_Area_Of_Walls)
_Total_Green_Paint = _Total_Area_Of_Walls / 3.4
print(f"{_Total_Green_Paint:.2f}")

# Roof
_Area_Of_Triangle = (_x * _h) / 2
_Total_Area_Of_Triangle = _Area_Of_Triangle * 2
#print(_Total_Area_Of_Triangle)

_Area_Of_Roof_Side = _x * _y
_Total_Area_Of_Roof_Side = _Area_Of_Roof_Side * 2
#print(_Total_Area_Of_Roof_Side)

_Total_Area_Of_Roof = _Total_Area_Of_Triangle + _Total_Area_Of_Roof_Side
#print(_Total_Area_Of_Roof)
_Total_Red_Paint = _Total_Area_Of_Roof / 4.3
print(f"{_Total_Red_Paint:.2f}")
