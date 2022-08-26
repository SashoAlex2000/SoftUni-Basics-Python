from math import floor, ceil


days = int(input())
food_left = int(input())
dogfood_per_day = float(input())
catfood_per_day = float(input())
tourtoisefood_per_day = float(input())

tourtoisefood_per_day /= 1000

total_food_needed = dogfood_per_day * days + catfood_per_day * days + tourtoisefood_per_day * days
difference = food_left - total_food_needed

if difference >= 0:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(abs(difference))} more kilos of food are needed.")
