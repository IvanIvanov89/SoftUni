ChickenMenu = int(input()) * 10.35
FishMenu = int(input()) * 12.40
VeganMenu = int(input()) * 8.15
SumMenu = ChickenMenu + FishMenu + VeganMenu
Dessert = SumMenu * 0.20
TotalFood = SumMenu + Dessert
TotalAmount = TotalFood + 2.50

print(TotalAmount)
