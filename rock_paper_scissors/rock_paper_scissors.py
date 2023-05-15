import random


def determine_relations(options):
    """
    This function determines the strong and weak element
    :param options:
    :return: relations
    """
    n = len(options)
    relations = {}
    for i in range(n):
        half = (n - 1) // 2
        weaker = options[i+1:i+1+half] + options[:i]
        stronger = options[i+1+half:] + options[i+1:i+1+half]
        relations[options[i]] = (weaker, stronger)
    return relations


def get_random_option(options):
    """
    this function selects a random element
    :param options:
    :return: random.choice(options)
    """
    return random.choice(options)


def determine_result(user_option, comp_option, relations):
    """
    this function selects the outcome of the game
    :param user_option:
    :param comp_option:
    :param relations:
    :return: result
    """
    if user_option == comp_option:
        return 'Draw'
    weaker, stronger = relations[user_option]
    if comp_option in weaker:
        return 'Lose'
    return 'Win'


def read_options(option_string):
    """
    function reads the options that the player sets
    :param option_string:
    :return:
    """
    options = option_string.split(',')
    options = [option.strip() for option in options]
    return options


def play_game(user_name, options):
    """
    main game function
    :param user_name:
    :param options:
    :return:
    """
    rating = 0
    relations = determine_relations(options)
    print("Okay, let's start.")

    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye!")
            break

        if user_input not in options:
            print("Invalid input")
            continue

        comp_option = get_random_option(options)
        result = determine_result(user_input, comp_option, relations)
        print(f"{result} -> The computer chose {comp_option}")

        if result == 'Draw':
            rating += 50
        elif result == 'Win':
            rating += 100

    with open("rating.txt", "a") as file:
        file.write(f"{user_name} {rating}\n")


user_name = input("Enter your name: ")
print(f"Hello, {user_name}")
user_options = input("Enter options (separated by commas): ").strip()
if user_options == "":
    user_options = "rock,paper,scissors"

options = read_options(user_options)
play_game(user_name, options)
