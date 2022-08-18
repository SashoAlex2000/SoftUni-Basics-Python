number_of_groups = int(input())

musala_group = 0
monblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0

total_people = 0

for i in range(number_of_groups):
    current_group = int(input())
    total_people += current_group
    if current_group <=5:
        musala_group += current_group
    elif current_group <=12:
        monblan_group += current_group
    elif current_group <= 25:
        kilimandjaro_group += current_group
    elif current_group <= 40:
        k2_group += current_group
    else:
        everest_group += current_group

print(f"{(musala_group/total_people)*100:.2f}%")
print(f"{(monblan_group/total_people)*100:.2f}%")
print(f"{kilimandjaro_group/total_people*100:.2f}%")
print(f"{k2_group/total_people*100:.2f}%")
print(f"{everest_group/total_people*100:.2f}%")

