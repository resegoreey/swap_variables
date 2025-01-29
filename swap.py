x = input("Input any x value: ")
y = input("Input any y value: ")

print(f"You have entered x = {x} and y = {y} before we swap them")

x, y = y, x
print()

print(f"""The variables are swapped now
     x = {x} and y = {y}""")