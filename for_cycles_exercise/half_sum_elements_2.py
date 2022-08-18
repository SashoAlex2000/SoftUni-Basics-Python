import sys

count_of_number = int(input())

sum_of_all = 0
max_number = -sys.maxsize

for number in range(count_of_number):
    current_number = int(input())
    sum_of_all += current_number
    if current_number > max_number:
        max_number = current_number


difference = abs(max_number- (sum_of_all - max_number))

if max_number == (sum_of_all -max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {difference}")


# difference = abs(max_number - (sum_of_all -max_number)
#
# if max_number == (sum_of_all - max_number):
#     print("Yes")
#     print(f"Sum = {max_number}")
#
# else:
#     print(f"No")
#     print(f"Diff = {difference}")
