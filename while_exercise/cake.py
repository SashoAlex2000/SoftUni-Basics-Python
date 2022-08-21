width = int(input())
lenght = int(input())

total_pieces = width * lenght

cake_is_over = False

command = input()

while command != "STOP":
    current_number_pieces = int(command)
    total_pieces -= current_number_pieces

    if total_pieces < 0:
        cake_is_over = True
        break

    command = input()

if cake_is_over:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")
else:
    print(f"{total_pieces} pieces are left.")