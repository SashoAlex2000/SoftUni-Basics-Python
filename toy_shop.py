price_holiday = float(input())

jigsaw_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

price_jigsaw = 2.6
price_doll = 3
price_teddy_bear = 4.1
price_minion = 8.2
price_truck = 2

item_count = jigsaw_count + doll_count +teddy_bear_count + minion_count + truck_count

money = jigsaw_count * price_jigsaw + doll_count * price_doll + teddy_bear_count * price_teddy_bear \
        + minion_count * price_minion + truck_count * price_truck

if item_count >= 50:
        money *= 0.75

money *= 0.9

difference = money - price_holiday

if difference >= 0:
        print(f"Yes! {difference:.2f} lv left.")
else:
        print(f"Not enough money! {abs(difference):.2f} lv needed.")

