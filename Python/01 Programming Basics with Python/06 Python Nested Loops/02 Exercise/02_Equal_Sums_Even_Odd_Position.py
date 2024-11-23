number_1 = int(input())
number_2 = int(input())

for idx in range(number_1, number_2 + 1):
    idx_string = str(idx)
    odd_sum = 0
    even_sum = 0
    for i, n in enumerate(idx_string):
        if i % 2 == 0:
            odd_sum += int(n)
        else:
            even_sum +=int(n)
    if odd_sum == even_sum:
        print(idx, end=' ')
