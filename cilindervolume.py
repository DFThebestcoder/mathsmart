print("-------------------------------------------------")
print("This program calculates the volume of a cylinder.")
print("-------------------------------------------------")
while True:
    user_text = input("put your radius in the box: ")
    try:
        radius = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
area = 3.14 * radius * radius
while True:
    user_text = input("put your height in the box: ")
    try:
        height = float(user_text)
        break
    except ValueError:
        print("Please enter a valid number, like 3.5 or 4.")
volume = area * height
print("volume is",volume)