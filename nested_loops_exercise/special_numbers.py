n = int(input())
is_special = False


for number in range(1111, 9999 + 1):
    # number_to_str = str(number)

    for digit in str(number):
        if int(digit) == 0:
            is_special = False
            break
        # elif int(digit) > n:
        #     is_special = False
        #     break

        elif n % int(digit) == 0:
            is_special = True
        elif n % int(digit) != 0:
            is_special = False
            break



    if is_special:
        print(number, end =" ")
