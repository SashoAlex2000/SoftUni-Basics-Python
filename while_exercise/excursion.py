needed_money = float(input())
starting_money = float(input())

total_day_counter = 0
spend_day_counter = 0

is_money_saved = True

while starting_money < needed_money:
    action = input()
    current_sum = float(input())
    total_day_counter += 1



    if action == "spend":
        starting_money -= current_sum
        if starting_money <= 0:
            starting_money = starting_money * 0
        spend_day_counter += 1

    if spend_day_counter == 5:
        is_money_saved = False
        break

    elif action == "save":
        starting_money += current_sum
        spend_day_counter = spend_day_counter * 0

if is_money_saved == False:
    print("You can't save the money.")
    print(total_day_counter)
else:
    print(f"You saved the money for {total_day_counter} days.")
