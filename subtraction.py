print("----------------------------------------------------")
print("this program calculates the substraction of numbers.")
print("----------------------------------------------------")
while True:
    user_text = input("put your numbers in the box separated by -: ")
    try:
        numbers = [float(x) for x in user_text.split('-')]
        break
    except ValueError:
        print("Please enter valid numbers, like 3.5 or 4.")
print("your answer is:", numbers[0] - sum(numbers[1:]))