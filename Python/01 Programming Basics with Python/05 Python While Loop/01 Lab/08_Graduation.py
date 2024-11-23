student = input()

all_marks = fails = 0
grade = 1

while True:
    mark = float(input())
    if mark < 4:
        fails += 1
        if fails > 1:
            print(f"{student} has been excluded at {grade} grade")
            break
        continue
    all_marks += mark
    if grade == 12:
        print(f'{student} graduated. Average grade: {all_marks / grade:.2f}')
        break

    grade += 1
