"""This is to run the program"""

from interface import *

# Test unit used to run and test program - Suraj
if __name__ == '__main__':

    # running welcome function and obtaining user name - Suraj
    user_name()

    # running user location - Suraj
    user_loc()

    # running first chatbot question, to obtain users feelings - Suraj
    user_feeling()

    # running weather function - Suraj
    weather_main()

    # running store function - Suraj
    stores_main()

# Creating while loop to run menu options - Suraj
x = 0
while x < 1:

    # running chabot user option selection - Suraj
    user_option()

    # run selection - Suraj
    selection()
    decision = choice['selection']
    decision = int(decision)
    if decision == 1:
        # run basic maths
        maths_main_2()
    if decision == 2:
        # run english
        english_main()
    if decision == 3:
        # Exit program
        exit()
        x = 1








