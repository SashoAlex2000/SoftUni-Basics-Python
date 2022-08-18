import sys
number = int(input())
total_sum = 0
max_number = -sys.maxsize

for i in range(number):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

difference = abs((total_sum - max_number) - max_number)

if total_sum / 2 == max_number:
    print("Yes")
    print(f"Sum = {(total_sum/2):.0f}")

else:
    print("No")
    print(f"Diff = {difference}")


# 3 != 3.00, zatova ne bi trqbvalo da raboti sus delenie na 2 :DD (?)