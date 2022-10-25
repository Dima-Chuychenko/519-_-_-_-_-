"""
    Chatbot by Dima Chuychenko
"""

print("Hello! My name is Chet.\n"
      "I was created in 20 October 2022.\n"
      "Please, remind me your name.")

"""
    here the user enters his name 
"""

name_input = input()

print("What a great name you have, ", name_input, "!\n"
                                                  "Let me guess your age.\n"
                                                  "Enter remainders of dividing your age by 3, 5 and 7.")

""" 
    here the user enters his remainders of the number
"""

remainders3 = int(input())
remainders5 = int(input())
remainders7 = int(input())

"""
    formula for calculating a number
"""

age = (remainders3 * 70 + remainders5 * 21 + remainders7 * 15) % 105

print("Your age is", age, "that's a good time to start programming!\n"
                          "Now I will prove to you that I can count to any number you want.")

""" 
    variable the user enters his random number
"""

number_input = int(input())

""" 
    custom number
"""

number = 0

""" 
    cycle while for count input number
"""

while number <= number_input:
    print(number, "!")
    number += 1

print("Completed!\n"
      "Let's test your programming knowledge.\n"
      "The following types of loops do not exist in Python:\n"
      "1) if\n"
      "2) for\n"
      "3) while\n")

""" 
    correct input variable
"""

answer = int(input())

""" 
    cycle while for choosing the correct option
"""

while answer != 1:
    print("Please, try again.")
    answer = int(input())

print("Congratulations, have a nice day!")
