print("-------------------------------------------------")
print("This program calculates the volume of a sphere.")
print("-------------------------------------------------")
while True:
    user_text = input("put your radius in the box: ")
    try:
        radius = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
volume = (4/3) * 3.14 * radius * radius * radius
print("volume is",volume)