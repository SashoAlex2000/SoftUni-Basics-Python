students = int(input())

top_students = 0
four_to_five = 0
three_to_four = 0
fail = 0
total_sum_of_grades = 0

for _ in range(students):
    current_grade = float(input())
    total_sum_of_grades += current_grade
    if current_grade < 3:
        fail += 1
    elif 3 <= current_grade < 4:
        three_to_four += 1
    elif 4 <= current_grade < 5:
        four_to_five += 1
    else:
        top_students += 1

average = total_sum_of_grades / students

print(f"Top students: {top_students / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {four_to_five / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {three_to_four / students * 100:.2f}%")
print(f"Fail: {fail / students * 100:.2f}%")
print(f"Average: {average:.2f}")

