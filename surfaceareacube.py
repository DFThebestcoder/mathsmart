print("---------------------------------------------------")
print("This program calculates the surface area of a cube.")
print("---------------------------------------------------")
while True:
    user_text = input("put your side length in the box: ")
    try:
        side_length = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
surface_area = 6 * (side_length * side_length)
print("surface area is", surface_area)