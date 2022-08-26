from math import floor, ceil

x_sq_meters = int(input())
y_grapes_from_1_sq = float(input())
z_needed_liters = int(input())
number_of_workers = int(input())

harvest = ((x_sq_meters * 0.4) * y_grapes_from_1_sq) / 2.5

difference = harvest - z_needed_liters

if harvest < z_needed_liters:
    print(f"It will be a tough winter! More {floor(z_needed_liters - harvest)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(harvest)} liters.")
    print(f"{ceil(harvest - z_needed_liters)} liters left -> {ceil(difference / number_of_workers)} liters per person.")
