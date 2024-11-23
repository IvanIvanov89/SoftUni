NylonSheet = int(input())
TotalNylonSheet = (NylonSheet + 2) * 1.50
Paint = int(input())
ExtraPaint = (Paint + (Paint * 0.10)) * 14.50
PaintWatter = int(input()) * 5
Package = 0.40
HorsForJobDone = int(input())

WorkHourPrice = (TotalNylonSheet + ExtraPaint + PaintWatter + Package) * 0.30
PriceForWorkers = WorkHourPrice * HorsForJobDone

Total = PriceForWorkers + TotalNylonSheet + ExtraPaint + PaintWatter + Package

print(Total)
