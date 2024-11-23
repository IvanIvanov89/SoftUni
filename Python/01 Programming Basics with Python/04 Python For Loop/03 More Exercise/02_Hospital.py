period = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for idx in range(1, period + 1, 1):
    if idx % 3 == 0 and treated_patients < untreated_patients:
        doctors += 1
    patients = int(input())
    if doctors >= patients:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += (patients - doctors)

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
