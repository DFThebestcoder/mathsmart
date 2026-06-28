import statistics


def calculate_statistics():
    print("----------------------------------------------------------------------------------------")
    print("This program calculates the mean, mode, median, average, and range of a list of numbers.")
    print("----------------------------------------------------------------------------------------")
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(x) for x in numbers]

    print("Mean:", statistics.mean(numbers))
    print("Median:", statistics.median(numbers))
    try:
        print("Mode:", statistics.mode(numbers))
    except statistics.StatisticsError:
        print("Mode: no unique mode")
    print("Range:", max(numbers) - min(numbers))


def get_float_input(prompt):
    while True:
        user_text = input(prompt).strip()
        try:
            return float(user_text)
        except ValueError:
            print("Please enter a valid number, like 3.5 or 4.")


while True:
    print("Choose an option:")
    print("1. surface area")
    print("2. volume")
    print("3. mmmar")
    user_text = input("Enter your choice: ").strip().lower()

    if user_text in ("1", "surface area"):
        while True:
            shape = input(
                "choose to calculate the Surface Area of a cylinder, cone, sphere, or cube: "
            ).strip().lower()
            if shape in ("cylinder", "cone", "sphere", "cube"):
                break
            print("Please type only: cylinder, cone, sphere, or cube.")

        if shape == "cylinder":
            print("-------------------------------------------------------")
            print("This program calculates the surface area of a cylinder.")
            print("-------------------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            height = get_float_input("put your height in the box: ")
            surface_area = 2 * 3.14 * radius * (radius + height)
            print("surface area is", surface_area)

        elif shape == "cone":
            print("---------------------------------------------------")
            print("This program calculates the surface area of a cone.")
            print("---------------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            height = get_float_input("put your height in the box: ")
            surface_area = 3.14 * radius * (radius + (height**2 + radius**2)**0.5)
            print("surface area is", surface_area)

        elif shape == "sphere":
            print("-----------------------------------------------------")
            print("This program calculates the surface area of a sphere.")
            print("-----------------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            surface_area = 4 * 3.14 * (radius * radius)
            print("surface area is", surface_area)

        elif shape == "cube":
            print("---------------------------------------------------")
            print("This program calculates the surface area of a cube.")
            print("---------------------------------------------------")
            side_length = get_float_input("put your side length in the box: ")
            surface_area = 6 * (side_length * side_length)
            print("surface area is", surface_area)

        break

    elif user_text in ("2", "volume"):
        while True:
            shape = input(
                "choose to calculate the volume of a cylinder volume, cone volume, sphere volume, or cube volume: "
            ).strip().lower()
            if shape in ("cylinder volume", "cone volume", "sphere volume", "cube volume"):
                break
            print("Please type only: cylinder volume, cone volume, sphere volume, or cube volume.")

        if shape == "cylinder volume":
            print("-------------------------------------------------")
            print("This program calculates the volume of a cylinder.")
            print("-------------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            height = get_float_input("put your height in the box: ")
            volume = 3.14 * radius * radius * height
            print("volume is", volume)

        elif shape == "cone volume":
            print("---------------------------------------------")
            print("This program calculates the volume of a cone.")
            print("---------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            height = get_float_input("put your height in the box: ")
            volume = (1 / 3) * 3.14 * radius * radius * height
            print("volume is", volume)

        elif shape == "sphere volume":
            print("-----------------------------------------------")
            print("This program calculates the volume of a sphere.")
            print("-----------------------------------------------")
            radius = get_float_input("put your radius in the box: ")
            volume = (4 / 3) * 3.14 * radius * radius * radius
            print("volume is", volume)

        elif shape == "cube volume":
            print("-----------------------------------------------")
            print("This program calculates the volume of a cube.")
            print("-----------------------------------------------")
            side_length = get_float_input("put your side length in the box: ")
            volume = side_length * side_length * side_length
            print("volume is", volume)

        break

    elif user_text in ("3", "mmmar"):
        calculate_statistics()
        break

    else:
        print("Please type only: surface area, volume, or mmmar.")