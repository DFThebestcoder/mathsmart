print("-----------------------------------------------------")
print("This program calculates the surface area of a sphere.")
print("-----------------------------------------------------")
while True:
    user_text = input("put your radius in the box: ")
    try:
        radius = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
surface_area = 4 * 3.14 * (radius * radius)
print("surface area is", surface_area)