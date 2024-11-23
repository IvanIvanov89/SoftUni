_Speed = float(input())

if _Speed <= 10:
    print("slow")
elif 10 < _Speed <= 50:
    print("average")
elif 50 < _Speed <= 150:
    print("fast")
elif 150 < _Speed <= 1000:
    print("ultra fast")
elif 1000 < _Speed:
    print("extremely fast")
