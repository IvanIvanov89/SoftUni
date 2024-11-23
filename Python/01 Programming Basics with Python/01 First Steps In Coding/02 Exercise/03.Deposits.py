DepSum = float(input())
DepPeriod = int(input())
YearIntrPercent = float(input())

YearIntrestAmaount = DepSum * (YearIntrPercent/100)

InterestPerMonth = YearIntrestAmaount / 12


Sum = DepSum + (DepPeriod * InterestPerMonth)

print(Sum)
#print(InterestPerMonth)

#print(YearIntrestAmaount)
