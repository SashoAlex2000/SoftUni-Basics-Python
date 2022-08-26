v = int(input())
p1 = int(input())
p2 = int(input())
hours_gone = float(input())

filled_liters = p1 * hours_gone + p2 * hours_gone
percent_filled = (filled_liters / v) * 100



if filled_liters < v:
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {((p1 / (p1 + p2)) * 100):.2f}%. "
          f"Pipe 2: {((p2 / (p1 + p2)) * 100):.2f}%.")
else:
    print(f"For {hours_gone:.2f} hours the pool "
          f"overflows with {filled_liters - v:.2f} liters.")