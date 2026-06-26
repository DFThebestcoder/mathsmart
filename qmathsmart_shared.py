PI = 3.14


def get_float_input(prompt):
    while True:
        user_text = input(prompt).strip()
        try:
            return float(user_text)
        except ValueError:
            print("Please enter a valid number, like 3.5 or 4.")


def get_choice(prompt, valid_choices):
    while True:
        user_text = input(prompt).strip().lower()
        if user_text in valid_choices:
            return user_text
        print(f"Please type only: {', '.join(valid_choices)}.")


def calculate_cylinder_volume(radius, height):
    return PI * radius * radius * height


def calculate_cylinder_surface_area(radius, height):
    return (2 * PI * radius * radius) + (2 * PI * radius * height)


def calculate_cone_volume(radius, height):
    return (1 / 3) * PI * radius * radius * height


def calculate_cone_surface_area(radius, height):
    return PI * radius * (radius + (height * height + radius * radius) ** 0.5)


def calculate_sphere_volume(radius):
    return (4 / 3) * PI * radius * radius * radius


def calculate_sphere_surface_area(radius):
    return 4 * PI * radius * radius


def calculate_cube_volume(side_length):
    return side_length * side_length * side_length


def calculate_cube_surface_area(side_length):
    return 6 * side_length * side_length


print("--------------------")
print("Welcome to MathSmart")
print("--------------------")

calculation_type = get_choice(
    "choose to calculate the Surface Area or volume: ",
    ("surface area", "volume"),
)

if calculation_type == "surface area":
    shape = get_choice(
        "choose to calculate the Surface Area of a cylinder, cone, sphere, or cube: ",
        ("cylinder", "cone", "sphere", "cube"),
    )
else:
    shape = get_choice(
        "choose to calculate the volume of a cylinder volume, cone volume, sphere volume, or cube volume: ",
        ("cylinder volume", "cone volume", "sphere volume", "cube volume"),
    )

if shape == "cylinder volume":
    print("-------------------------------------------------")
    print("This program calculates the volume of a cylinder.")
    print("-------------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    height = get_float_input("put your height in the box: ")
    print("volume is", calculate_cylinder_volume(radius, height))

elif shape == "cylinder":
    print("-------------------------------------------------------")
    print("This program calculates the surface area of a cylinder.")
    print("-------------------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    height = get_float_input("put your height in the box: ")
    print("surface area is", calculate_cylinder_surface_area(radius, height))

elif shape == "cone volume":
    print("---------------------------------------------")
    print("This program calculates the volume of a cone.")
    print("---------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    height = get_float_input("put your height in the box: ")
    print("volume is", calculate_cone_volume(radius, height))

elif shape == "cone":
    print("---------------------------------------------------")
    print("This program calculates the surface area of a cone.")
    print("---------------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    height = get_float_input("put your height in the box: ")
    print("surface area is", calculate_cone_surface_area(radius, height))

elif shape == "sphere volume":
    print("-----------------------------------------------")
    print("This program calculates the volume of a sphere.")
    print("-----------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    print("volume is", calculate_sphere_volume(radius))

elif shape == "sphere":
    print("-----------------------------------------------------")
    print("This program calculates the surface area of a sphere.")
    print("-----------------------------------------------------")
    radius = get_float_input("put your radius in the box: ")
    print("surface area is", calculate_sphere_surface_area(radius))

elif shape == "cube volume":
    print("-----------------------------------------------")
    print("This program calculates the volume of a cube.")
    print("-----------------------------------------------")
    side_length = get_float_input("put your side length in the box: ")
    print("volume is", calculate_cube_volume(side_length))

elif shape == "cube":
    print("---------------------------------------------------")
    print("This program calculates the surface area of a cube.")
    print("---------------------------------------------------")
    side_length = get_float_input("put your side length in the box: ")
    print("surface area is", calculate_cube_surface_area(side_length))
