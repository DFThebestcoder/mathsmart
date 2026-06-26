print("-------------------------------------------------------")
print("This program calculates the surface area of a cylinder.")
print("-------------------------------------------------------")
while True:
    user_text = input("put your radius in the box: ")
    try:
        radius = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
area = 3.14 * radius * radius * 2
circumference = 2 * 3.14 * radius
while True:
    user_text = input("put your height in the box: ")
    try:
        height = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
surface_area = area + (circumference * height)
print("surface area is",surface_area)