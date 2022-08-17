budget = float(input())
extra_number = int(input())
price_clothes = float(input())

decoration = 0.1 * budget
if extra_number > 150:
    price_clothes *= 0.9

extra_cost = extra_number * price_clothes
cost = extra_cost + decoration

difference = budget - cost

if difference >= 0:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {abs(difference):.2f} leva more.")