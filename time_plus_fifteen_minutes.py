from math import floor
hours = int(input())
minutes = int(input())

time = hours * 60 + minutes

future_time = time + 15

future_hours = floor(future_time / 60)
future_minutes = future_time % 60

if future_hours == 24:
    future_hours = 0


if future_minutes < 10:
    print(f"{future_hours}:0{future_minutes}")
else:
    print(f"{future_hours}:{future_minutes}")