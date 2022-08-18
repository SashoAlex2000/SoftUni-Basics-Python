age = int(input())
price_of_laundry = float(input())
price_of_toy = int(input())

money_saved = 0
total_toys = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        new_money = (i / 2) * 10
        money_saved += new_money - 1
    else:
        total_toys += 1

total_money = money_saved + (total_toys * price_of_toy)
difference = abs(total_money - price_of_laundry)

if total_money >= price_of_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
