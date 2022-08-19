period = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, period + 1):
    if i % 3 != 0:
        current_patients = int(input())
        if current_patients <= doctors:
            treated_patients += current_patients

        elif current_patients > doctors:
            treated_patients += doctors
            untreated_patients = untreated_patients + current_patients - doctors

    elif i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
        else:
            pass
        current_patients = int(input())
        if current_patients <= doctors:
            treated_patients += current_patients

        elif current_patients > doctors:
            treated_patients += doctors
            untreated_patients = untreated_patients + current_patients - doctors



print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
