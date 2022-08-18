n = int(input())

double_n = 2 * n
first_sum = 0
second_sum = 0

for i in range(n):
    current_number = int(input())
    first_sum += current_number

for i in range(n):
    current_number = int(input())
    second_sum += current_number

difference = abs(second_sum - first_sum)

if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f"No, diff = {difference}")

