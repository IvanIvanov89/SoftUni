start = input()
end = input()

start_string = str(start)
end_string = str(end)

start1, start2, start3, start4 = map(int, start)
end1, end2, end3, end4 = map(int, end)

for one in range(start1, end1 + 1):
    if one % 2 == 0:
        continue
    for two in range(start2, end2 + 1):
        if two % 2 == 0:
            continue
        for three in range(start3, end3 + 1):
            if three % 2 == 0:
                continue
            for four in range(start4, end4 + 1):
                if four % 2 == 0:
                    continue
                print(f'{one}{two}{three}{four}', end= ' ')
