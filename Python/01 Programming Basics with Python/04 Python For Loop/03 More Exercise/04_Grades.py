students = int(input())

up_to_2_99 = 0
up_to_3_99 = 0
up_to_4_99 = 0
up_to_6 = 0

all_marks = 0

for _ in range(students):
    mark = float(input())

    if mark <= 2.99:
        all_marks += mark
        up_to_2_99 += 1
    elif mark <= 3.99:
        all_marks += mark
        up_to_3_99 += 1
    elif mark <= 4.99:
        all_marks += mark
        up_to_4_99 += 1
    else:
        all_marks += mark
        up_to_6 += 1

percent_1 = (up_to_2_99 / students) * 100
percent_2 = (up_to_3_99 / students) * 100
percent_3 = (up_to_4_99 / students) * 100
percent_4 = (up_to_6 / students) * 100
average_mark = all_marks / students
print(f'Top students: {percent_4:.2f}%')
print(f'Between 4.00 and 4.99: {percent_3:.2f}%')
print(f'Between 3.00 and 3.99: {percent_2:.2f}%')
print(f'Fail: {percent_1:.2f}%')
print(f'Average: {average_mark:.2f}')
