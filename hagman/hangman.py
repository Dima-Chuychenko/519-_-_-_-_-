import random

while True:

    print("Type \"play\" to play the game, \"exit\" to quit:> ", end="")
    action_type = ("play", "exit")
    user_input = input()

    while user_input != "play" and user_input != "exit":
        print("Write some action:> ", end="")
        user_input = input()

    if user_input == "play":
        word_tuple = ('python', 'java', 'javascript', 'php')
        random_words = random.choice(word_tuple)
        # encrypted_word = random_words
        # encrypted_word = [str(i) for i in encrypted_word]
        # encrypted_word[3:] = ['-'] * len(encrypted_word)
        encrypted_word = ['-'] * len(random_words)

        # print('' .join(encrypted_word))

        print("HANGMAN\n"
              "The game will be available soon\n"
              "Guess the word", ''.join(encrypted_word), ":> ", end="")

        num_of_chance = 8
        found_letter = []

        while num_of_chance > 0 and ''.join(encrypted_word) != random_words:

            letter = input()

            if letter != letter.lower():
                print("Please enter a lowercase English latter.")
                continue

            if len(letter) > 1:
                print("You should input a single letter.")
                continue

            if letter in found_letter:
                print("You`ve already guessed this letter.\nLeft ", num_of_chance, " chance.")
                continue

            found_letter.append(letter)

            if letter in random_words:
                for i in range(len(random_words)):
                    if random_words[i] == letter:
                        encrypted_word[i] = letter
                print(''.join(encrypted_word))
            else:
                num_of_chance -= 1
                print("That letter doesn't appear in the word.\n"
                      "left ", num_of_chance, " chance.\n"
                                              "Guess the word", ''.join(encrypted_word), ":> ", end="")

        if num_of_chance == 0:
            print("\nYou lost!\n")
        else:
            print("\nYou survived!\n")

    if user_input == "exit":
        break
