
while True:
    user_text = input(
        "choose to calculate the Surface Area or volume: "
    ).strip().lower()
    if user_text in ("surface area", "volume"):
        break
    print("Please type only: surface area or volume.")
if user_text == "surface area":
    while True:
        user_text = input(
            "choose to calculate the Surface Area of a cylinder, cone, sphere, or cube: "
        ).strip().lower()
        if user_text in ("cylinder", "cone", "sphere", "cube"):
            break
        print("Please type only: cylinder, cone, sphere, or cube.")
if user_text == "volume":
    while True:
        user_text = input(
            "choose to calculate the volume of a cylinder volume, cone volume, sphere volume, or cube volume: "
        ).strip().lower()
        if user_text in ("cylinder volume", "cone volume", "sphere volume", "cube volume"):
            break
        print("Please type only: cylinder volume, cone volume, sphere volume, or cube volume.")

if user_text == "cylinder volume":
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
    print("volume is", volume)

elif user_text == "cylinder":
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
    circumference = 2 * 3.14 * radius
    while True:
        user_text = input("put your height in the box: ")
        try:
            height = float(user_text)
            break
        except ValueError:
            print("Please enter a valid number, like 3.5 or 4.")
    surface_area = circumference * (radius + height)
    print("surface area is", surface_area)

elif user_text == "cone volume":
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
    print("volume is", volume)

elif user_text == "cone":
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

elif user_text == "sphere volume":
    print("-----------------------------------------------")
    print("This program calculates the volume of a sphere.")
    print("-----------------------------------------------")
    while True:
        user_text = input("put your radius in the box: ")
        try:
            radius = float(user_text)
            break
        except ValueError:
            print("Please enter a valid number, like 3.5 or 4.")
    volume = (4/3) * 3.14 * radius * radius * radius
    print("volume is", volume)

elif user_text == "sphere":
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

elif user_text == "cube volume":
    print("-----------------------------------------------")
    print("This program calculates the volume of a cube.")
    print("-----------------------------------------------")
    while True:
        user_text = input("put your side length in the box: ")
        try:
            side_length = float(user_text)
            break
        except ValueError:
            print("Please enter a valid number, like 3.5 or 4.")
    volume = side_length * side_length * side_length
    print("volume is", volume)

elif user_text == "cube":
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