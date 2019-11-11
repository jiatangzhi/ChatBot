"""This is to run the program"""

from interface import user_name, user_feeling, user_option
from interface import selection, maths_main, choice, english_main, weather_main, stores_main

if __name__ == '__main__':

    # running welcome function and obtaining user name
    user_name()

    # running first chatbot question, to obtain users feelings
    user_feeling()

    # running chabot user option selection
    user_option()

    # run selection
    selection()
    decision = choice['selection']
    decision = int(decision)
    if decision == 1:
        # run basic maths
        maths_main()
    if decision == 2:
        # run english
        english_main()
    if decision == 3:
        # run weather function
        weather_main()
    if decision == 4:
        # run stores function
        restart = True
        while restart :
            restart = stores_main()







