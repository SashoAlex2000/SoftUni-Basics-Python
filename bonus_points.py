number = int(input())
five_bonus = 0
even_bonus = 0

if number <= 100:
    bonus = 5
if number > 100:
    bonus = 0.2 * number
if number > 1000:
    bonus = 0.1 * number
if number % 2 == 0:
    even_bonus = even_bonus + 1

if number % 10 == 5:
    five_bonus = five_bonus + 2


bonus_points = bonus + even_bonus + five_bonus
total_points = bonus_points + number

print(bonus_points)
print(total_points)
