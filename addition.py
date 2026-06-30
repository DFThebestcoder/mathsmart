print("------------------------------------------------")
print("This program calculates the addition of numbers.")
print("------------------------------------------------")
while True:
    user_text = input("put your numbers in the box separated by +: ")
    try:
        numbers = [float(x) for x in user_text.split('+')]
        break
    except ValueError:
        print("Please enter valid numbers, like 3.5 or 4.")

print("The sum of the numbers is:", sum(numbers))