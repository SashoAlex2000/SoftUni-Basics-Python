number_of_bad_marks = int(input())
total_grades = 0
did_he_pass = False
failed_marks = 0
number_of_problems = 0


name_of_problem = input()
grade = float(input())

while True:

    if grade > 4:
        total_grades += grade
        number_of_problems += 1
        name_of_problem = input()
        grade = float(input())

    if name_of_problem == 'Enough':
        did_he_pass = True
        break

    if grade <= 4:
        failed_marks += 1
        total_grades += grade
        number_of_problems += 1
        name_of_problem = input()
        grade = float(input())

    if failed_marks >= number_of_bad_marks:
        did_he_pass = False
        break


if did_he_pass == True:
    print(f"Average score: {total_grades / total_grades}")
    print(f"Number of problems: {total_grades}")
    print(f"Last problem: {name_of_problem}")



