print("----------------------------------------------------------------")
print("This program calculates the addition and subtraction of numbers.")
print("----------------------------------------------------------------")

while True:
    user_text = input("put your numbers in the box separated by + and -: ")
    user_text = user_text.replace(" ", "")

    # Only allow digits, dot, plus and minus
    if any(ch not in "0123456789.+-" for ch in user_text):
        print("Please enter valid numbers, like 3.5 or 4.")
        continue

    try:
        tokens = []
        number = ""

        for ch in user_text:
            if ch in "+-":
                if number != "":
                    tokens.append(float(number))
                number = ch
            else:
                number += ch

        if number:
            tokens.append(float(number))

        result = sum(tokens)
    except ValueError:
        print("Please enter valid numbers, like 3.5 or 4.")
        continue

    print("your answer is:", result)
    break