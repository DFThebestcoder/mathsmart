print("---------------------------------------------")
print("This program calculates the volume of a cone.")
print("---------------------------------------------")
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
volume = (1/3) * area * height
print("volume is",volume)