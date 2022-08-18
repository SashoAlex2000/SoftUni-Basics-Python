open_tabs = int(input())
salary = float(input())

is_salary_over = False

for i in range(open_tabs):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    if salary <= 0:
        is_salary_over = True
        break
    else:
        continue

if is_salary_over == True:
    print("You have lost your salary.")
else:
    print(round(salary))

