budget = float(input())
videocard = int(input())
gpu = int(input())
ram = int(input())

videocard_price = videocard * 250
gpu_price = gpu * (videocard_price * 0.35)
ram_price = ram * (videocard_price * 0.1)

total_cost = videocard_price + gpu_price + ram_price

if videocard > gpu:
    total_cost *= 0.85
else:
    pass

difference = budget - total_cost

if difference >= 0:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")


