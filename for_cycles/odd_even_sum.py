#
number = int(input())
odd_sum = 0
even_sum = 0

for num in range(number):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number

    else:
        odd_sum += current_number

difference = abs(even_sum - odd_sum)

if difference == 0:
    print("Yes")
    print(f"Sum = {even_sum}")

else:
    print("No")
    print(f"Diff = {difference}")
