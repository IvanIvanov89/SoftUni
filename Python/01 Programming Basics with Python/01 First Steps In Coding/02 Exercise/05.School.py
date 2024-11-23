PackOfPencils = int(input()) * 5.80
# 5.80 for 1 Pack
PackOfMarkers = int(input()) * 7.20
#7.20 for 1 Pack
LiterCleaner = int(input()) * 1.20
#1.20 for 1 Liter
DiscountPercent = int(input()) / 100

#PriceForPencils = PackOfPencils * 5.80
#print(PriceForPencils)
#PriceForMarkers = PackOfMarkers * 7.20
#print(PriceForMarkers)
#PriceForCleaner = LiterCleaner * 1.20
#print(PriceForCleaner)
#Discount = DiscountPercent / 100
#print(Discount)

TotalPrice = (PackOfPencils + PackOfMarkers + LiterCleaner)
#print(TotalPrice)
TotalAmount = TotalPrice - (TotalPrice*DiscountPercent)
print(TotalAmount)
