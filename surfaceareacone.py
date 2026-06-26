print("---------------------------------------------------")
print("This program calculates the surface area of a cone.")
print("---------------------------------------------------")
while True:
    user_text = input("put your radius in the box: ")
    try:
        radius = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")

while True:
    user_text = input("put your height in the box: ")
    try:
        height = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
surface_area = 3.14 * radius * (radius + (height**2 + radius**2)**0.5)
print("surface area is",surface_area)