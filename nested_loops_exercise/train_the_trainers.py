number_of_jourie = int(input())
total_averages = 0
total_participants = 0

command = input()

while command != "Finish":
    current_total = 0
    for i in range(1, number_of_jourie + 1):
        current_grade = float(input())
        current_total += current_grade
    current_average = current_total / number_of_jourie
    print(f"{command} - {current_average:.2f}.")

    total_averages += current_average
    total_participants += 1
    current_total = 0
    command = input()

print(f"Student's final assessment is {total_averages / total_participants:.2f}.")


