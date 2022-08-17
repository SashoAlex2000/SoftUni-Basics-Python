n1 = int(input())
n2 = int(input())
operator = input()
sum = 0

if (operator == "/" or operator == "%") and n2 == 0:
    print(f"Cannot divide {n1} by zero")
    exit()
else:
    pass


if operator == "+":
    sum = n1 + n2

elif operator == "-":
    sum = n1 - n2

elif operator == "*":
    sum = n1 * n2

elif operator == "/":
    sum = n1 / n2

elif operator == "%":
    sum = n1 % n2


oddness = ""
if sum % 2 == 0:
    oddness = "even"
else:
    oddness = "odd"

if operator == "+" or operator == "-" or operator == "*":
    print(f"{n1} {operator} {n2} = {sum} - {oddness}")

elif operator == "/":
    print(f"{n1} / {n2} = {sum:.2f}")


elif operator == "%":
    print(f"{n1} % {n1} = {sum}")






