starting_point = int(input())
ending_point = int(input())

magical_number = int(input())
counter = 0
number_is_found = False
magical_counter = 0

for n1 in range(starting_point , ending_point + 1):
    for n2 in range(starting_point, ending_point + 1):
        sum = n1 + n2
        counter += 1
        if sum == magical_number:
            number_is_found = True
            magical_counter = counter
            break
    if number_is_found == True:
        break

if number_is_found:
    print(f"Combination N:{magical_counter} ({n1} + {n2} = {magical_number})")
else:
    print(f"{counter} combinations - neither equals {magical_number}")


