n = int(input())
time_of_day = str(input())

if time_of_day == "day":
    taxi = 0.7 + n * 0.79
elif time_of_day == "night":
    taxi = 0.7 + n * 0.9

bus = n * 0.09
train = n * 0.06


if n < 20:
    print(f"{taxi:.2f}")
elif 20 <= n < 100:
    print(f"{bus:.2f}")
else:
    print(f"{train:.2f}")

