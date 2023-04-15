import random


def choice_level():
    level_input = input("Which level do you want?\n"
                        "1 - simple operations with numbers 2-9\n"
                        "2 - integral squares of 11-29\n"
                        "Enter a number: ")
    return level_input


level = choice_level()


def calculation():
    global level
    operation = random.choice(["*", "+", "-"])
    first_num = random.randint(1, 9)
    second_num = random.randint(1, 9)
    integral_squares = random.randint(11, 29)
    result = 0
    if level == "1":
        if operation == "*":
            result += first_num * second_num
        elif operation == "+":
            result += first_num + second_num
        elif operation == "-":
            result += first_num - second_num
        print(first_num, operation, second_num)
    elif level == "2":
        result += integral_squares * integral_squares
        print(integral_squares)
    return result


def test():
    global level
    truth = 0
    item = 0
    while item < 5:
        try:
            calculate = calculation()
            user_input = int((input("> ")))
            if user_input == calculate:
                print("Truth\n")
                truth += 1
                item += 1
            else:
                print("False\n")
                item += 1
        except ValueError:
            print("Incorrect format. Try again.")
    save_input = input(f"Your mark is {truth}/5.\n"
                       "Would you like to save the result? Enter yes or no.\n")
    if save_input == "yes":
        name_input = input("What is your name? ")
        with open("results.txt", "a") as f:
            f.write(f"Name: {name_input} {truth}/5 in level {level}\n")
            print("The results are saved in 'results.txt'.")
    else:
        print("Good Luck!")


test()
