from math import floor

needed_hours = int(input())
days = int(input())
number_of_overtime_employees = int(input())

hours_available = (days * 8) * 0.9
overtime_hours = number_of_overtime_employees * days * 2

total_hours = hours_available + overtime_hours

difference = total_hours - needed_hours

if difference >= 0:
    print(f"Yes!{floor(difference)} hours left.")
else:
    print(f"Not enough time!{abs(floor(difference))} hours needed.")