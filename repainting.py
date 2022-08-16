nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours_needed = int(input())

needed_paint =  1.1 * paint
needed_nylon = nylon + 2

materials_payment = needed_nylon * 1.5 + needed_paint * 14.5 + paint_thinner * 5 + 0.4
hourly_wage = 0.3 * materials_payment

total_sum = materials_payment + hourly_wage * hours_needed
print(total_sum)
