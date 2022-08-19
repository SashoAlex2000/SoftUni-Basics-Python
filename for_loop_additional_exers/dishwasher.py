import sys

number_of_detergent_bottles = int(input())
amount_of_detergent = number_of_detergent_bottles * 750

is_detergent_over = False

plates_washed = 0
pots_washed = 0

for i in range(1, sys.maxsize):
    if i % 3 != 0:
        thing_to_wash = input()
        if thing_to_wash == "End":
            break
        else:
            thing_to_wash = int(thing_to_wash)
            continue
        plates_to_wash = thing_to_wash * 1
        detergent_used = plates_to_wash * 5
        amount_of_detergent -= detergent_used
        plates_washed += plates_to_wash
    elif i % 3 == 0:
        thing_to_wash = input()
        if thing_to_wash == "End":
            break
        else:
            thing_to_wash = int(thing_to_wash)
            continue
        pots_to_wash = thing_to_wash * 1
        detergent_used = pots_to_wash * 15
        amount_of_detergent -= detergent_used
        pots_washed += pots_to_wash

    if amount_of_detergent <= 0:
        is_detergent_over = True
        break

if is_detergent_over == False:
    print("Detergent was enough!")
    print(f"{plates_washed} dishes and {pots_washed} pots were washed.")
    print(f"Leftover detergent {amount_of_detergent} ml.")

