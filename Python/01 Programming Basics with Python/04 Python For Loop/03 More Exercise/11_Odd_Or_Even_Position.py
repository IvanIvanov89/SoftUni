import sys

n = int(input())

OddMin = sys.maxsize
OddMax = -sys.maxsize
OddSum = 0

EvenMin = sys.maxsize
EvenMax = -sys.maxsize
EvenSum = 0

for idx in range(1, n + 1):
    number = float(input())

    if idx % 2 != 0:
        OddSum += number
        if OddMin > number:
            OddMin = number
        if OddMax < number:
            OddMax = number
    else:
        EvenSum += number
        if EvenMin > number:
            EvenMin = number
        if EvenMax < number:
            EvenMax = number

if n == 0:
    print(f'OddSum={OddSum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={EvenSum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif n == 1:
    print(f'OddSum={OddSum:.2f},')
    print(f'OddMin={OddMin:.2f},')
    print(f'OddMax={OddMax:.2f},')
    print(f'EvenSum={EvenSum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={OddSum:.2f},')
    print(f'OddMin={OddMin:.2f},')  # or No
    print(f'OddMax={OddMax:.2f},')  # or No
    print(f'EvenSum={EvenSum:.2f},')
    print(f'EvenMin={EvenMin:.2f},')  # or No
    print(f'EvenMax={EvenMax:.2f}')  # or No
