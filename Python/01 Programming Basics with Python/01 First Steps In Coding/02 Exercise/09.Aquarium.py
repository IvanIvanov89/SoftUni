Long = int(input())
Wide = int(input())
Height = int(input())
Percent = float(input())

TotalCDM = Long * Wide * Height
#print(TotalCDM)

VolumeInLiters = TotalCDM / 1000

Space = Percent / 100
#print(Space)

NeededLiters = VolumeInLiters *  (1 - Space)

print(NeededLiters)
