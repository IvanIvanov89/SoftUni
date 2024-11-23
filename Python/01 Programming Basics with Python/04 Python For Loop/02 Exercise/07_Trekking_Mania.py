groups = int(input())

mount_musala = 0
mount_monblan = 0
mount_kilimandjaro = 0
mount_k2 = 0
mount_everest = 0

total_people = 0

for _ in range(groups):
    people_in_group = int(input())
    total_people += people_in_group

    if people_in_group <= 5:
        mount_musala += people_in_group
    elif people_in_group <= 12:
        mount_monblan += people_in_group
    elif people_in_group <= 25:
        mount_kilimandjaro += people_in_group
    elif people_in_group <= 40:
        mount_k2 += people_in_group
    elif people_in_group >= 41:
        mount_everest += people_in_group

print(f'{mount_musala / total_people * 100:.2f}%')
print(f'{mount_monblan / total_people * 100:.2f}%')
print(f'{mount_kilimandjaro / total_people * 100:.2f}%')
print(f'{mount_k2 / total_people * 100:.2f}%')
print(f'{mount_everest / total_people * 100:.2f}%')
