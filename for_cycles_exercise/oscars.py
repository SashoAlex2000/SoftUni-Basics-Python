#sus is_nominated = false v nachaloto i tru pri break-a

name_of_actor = input()
total_points = float(input())
number_of_critics = int(input())


for i in range(number_of_critics):
    name = input()
    new_points = float(input())
    name_length = len(name)
    points_to_add = new_points * name_length / 2
    total_points += points_to_add
    if total_points >= 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
        break


if total_points < 1250.5:
    print(f"Sorry, {name_of_actor} you need {1250.5 - total_points:.1f} more!")
