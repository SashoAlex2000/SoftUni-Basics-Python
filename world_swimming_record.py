from math import floor

current_record = float(input())
distance = float(input())
swimming_speed = float(input())

ivan_speed = distance * swimming_speed

resistance = (floor(distance / 15)) * 12.5

ivan_speed = ivan_speed + resistance

difference = ivan_speed - current_record

if difference < 0:
    print(f"Yes, he succeeded! The new world record is {ivan_speed:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")
