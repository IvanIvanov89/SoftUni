AnnualPriceForTraining = int(input())

BacketShoes = AnnualPriceForTraining - (AnnualPriceForTraining * 0.40)
#print(BacketShoes)
BacketWear = BacketShoes - (BacketShoes * 0.20)
#print(BacketWear)
BacketBall = BacketWear / 4
#print(BacketBall)
BacketAccs = BacketBall / 5
#print(BacketAccs)

TotalForAnnual = AnnualPriceForTraining + BacketShoes + BacketWear + BacketBall + BacketAccs

print(TotalForAnnual)
