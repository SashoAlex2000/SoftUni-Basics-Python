
name = input()
grade_counter = 0
total_grades = 0
failed_exams = 0
is_dropped_out = False

grade_to_divide_by = 0

while True:
    current_grade = float(input())
    grade_counter += 1
    if current_grade >= 4:
        total_grades += current_grade
        grade_to_divide_by += 1

    if current_grade < 4:
        failed_exams += 1
    if failed_exams >= 2:
        is_dropped_out = True
    if is_dropped_out == True:
        break
    if grade_counter >= 12:
        break

if failed_exams >= 1:
    pass

if is_dropped_out == True:
    print(f"{name} has been excluded at {grade_counter - 1} grade")
else:
    print(f"{name} graduated. Average grade: {total_grades / grade_to_divide_by:.2f}")