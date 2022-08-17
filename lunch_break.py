from math import ceil

name_of_series = str(input())
length_of_episode = int(input())
break_lenght = int(input())

# lunch_time = break_lenght / 8
# leisure_time = break_lenght / 4

remaining_time = break_lenght * 5 / 8

difference = remaining_time - length_of_episode

if difference >= 0:
    print(f"You have enough time to watch {name_of_series} and left with {ceil(difference)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {ceil(abs(difference))} more minutes.")