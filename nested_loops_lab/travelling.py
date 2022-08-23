destination = input()
budget_needed = float(input())
current_budget = 0

while destination != "End":
    while current_budget < budget_needed:
        money_saved = float(input())
        current_budget += money_saved
        if current_budget >= budget_needed:
            print(f"Going to {destination}!")
            current_budget = 0
            break
    destination = input()
    if destination == "End":
        break
    budget_needed = float(input())


