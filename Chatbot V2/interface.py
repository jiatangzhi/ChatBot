"""To accept user inputs from the keyboard"""

from process import *
from data import user
import requests
import json
from dictionary import convo_words, keywords

# Empty dictionary for choice - Suraj
choice = {}


# Function to display welcome message and take user name as input to be written into empty dictionary - Suraj
def user_name():
    process_welcome_message()
    empty_line()
    name = input("What is your name? ")
    empty_line()
    process_user_name(name)
    print("Hello " + name)


# Function to take users location as input and return through process function - Suraj
def user_loc():
    empty_line()
    location = input("What city are you currently in? ")
    empty_line()
    process_user_location(location)


# This function calls on the self-created dictionaries to generate
# an intelligent response to the user based on how the user is feeling - Suraj
def user_feeling():
    name = user_data['name']
    feeling = input("How are you today? ").lower()
    sentence = feeling.split()
    empty_line()
    # Running the users input in a loop to check if any word appears in dictionary
    for word in sentence:
        if word in convo_words:
            # Pulling key value if word in dictionary returns True
            data = convo_words.get(word, "")
            # If-Else statements used to return intelligent response to the user
            if data == 0:
                print("Oh " + name + ", that is not so good to hear. Hopefully we can change that!")
                empty_line()
                break
            elif data == 1:
                print("Ahh, could be better then, let's see if we can improve that for you!")
                empty_line()
                break
            elif data == 2:
                print("That is good to hear " + name)
                empty_line()
                break
            elif data == 3:
                print("Wow, that's great " + name + "!")
                empty_line()
                break
            elif data < 0:
                print("Oh no, i am sorry to hear that " + name + ", hopefully I can help you cheer up!")
                empty_line()
                break
            else:
                continue
    # Second loop is run to test if the user has asked the question back to the user
    for secondary in sentence:
        if secondary in keywords:
            data = keywords.get(secondary, "")
            if data == 1:
                print("I am great, and excited to help you, thank you for asking!")
                empty_line()
                break
            else:
                continue


# This function takes the users option choice and validates it against possible responses - Suraj
# If the selection is invalid, the user will be told and given another chance to make the right selection
def user_option():
    name = user_data['name']
    x = 0
    process_user_option()
    while x < 1:
        selection = input("Please select either option 1, 2 or 3: ")
        empty_line()
        # Writing the users selection to the empty dictionary
        choice['selection'] = selection
        user.append(choice)
        selectionInt = int(selection)
        if (selectionInt > 0) and (selectionInt < 4):
            x = 1
        else:
            print("I'm sorry " + name + ", that is an invalid option! Please try again")
            empty_line()
            x = 0


# This function takes the users selection and runs it, whilst involving extra parameters for interaction - Suraj
def selection():
    x = 0
    # Importing user name and selection from dictionaries
    name = user_data['name']
    decision = choice['selection']
    decision = int(decision)
    # If else statements to run selections whilst providing options to leave the option - Suraj
    if decision == 1:
        process_maths_welcome()
        while x < 1:
            continuation = input("")
            empty_line()
            if ('ye' in continuation) or ('sure' in continuation) or ('ok' in continuation) or ('not' in continuation):
                print("Let's get started then!")
                x = 1
                empty_line()
            elif ('no' in continuation) or ('na' in continuation):
                print("Okay " + name + ", maybe next time.")
                x = 1
                exit()
            else:
                # error case
                print("Sorry " + name + ", that is not a valid selection, please try again!")
                x = 0

    elif decision == 2:
        process_english_welcome()
        while x < 1:
            continuation = input("")
            empty_line()
            if ('ye' in continuation) or ('sure' in continuation) or ('ok' in continuation) or ('not' in continuation):
                print("Let's get started then!")
                x = 1
                empty_line()
            elif ('no' in continuation) or ('na' in continuation):
                print("Okay " + name + ", maybe next time.")
                x = 1
                exit()
            else:
                # error case
                print("Sorry " + name + ", that is not a valid selection, please try again!")
                x = 0

    elif decision == 3:
        print("It was nice talking to you!")
        exit()


def maths_main():
    process_maths_question()
    ans = input("Your answer: ")
    ans = int(ans)
    if ans == 2:
        print("Well done! That is correct")
    else:
        print("Oh no, unfortunately that is not correct")
        print("Would you like me to explain?")
        decision = input("")
        if ('ye' in decision) or ('okay' in decision) or ('sure' in decision):
            print("Firstly we minus 6 from 10, which leaves;")
            print('2a = 4')
            empty_line()
            print("Then we divide 4 by 2, which gives the answer;")
            print("a = 2")
            empty_line()
            print("Does that make sense?")
            decision2 = input("")
            print("Great!")
        else:
            print("Okay, maybe next time!")


# This function tests the user on basic GCSE algebraic maths - Suraj
# The function will ask the user several questions and create a txt file for the user upon completion
# the txt file will display the test results question by question
def maths_main_2():
    # creating txt file for users test
    f = open("userTest.txt", "w")
    print("Your test will now begin.")
    empty_line()
    print("Question 1: " + "\n5a - 20 = 40 // What is the value of a?")
    f.write("Question 1: 5a - 20 = 40 // What is the value of a?")
    answer1 = int(input())
    f.write("\n" + str(answer1))
    empty_line()
    if answer1 == 12:
        score = 1
        f.write("\nCorrect")
    else:
        score = 0
        f.write("\nIncorrect")
        f.write("\nThe correct answer is: 12")
    print("Question 2: " + "\nSimplify the linear equation: 5a + 7a - 12b + 4b = 30")
    f.write("\n\nQuestion 2: Simplify the linear equation: 5a + 7a - 12b + 4b = 30")
    answer2 = input()
    f.write("\n" + str(answer2))
    empty_line()
    if answer2 == '12a - 16b = 30':
        score = score + 1
        f.write("\nCorrect")
    else:
        score = score
        f.write("\nIncorrect")
        f.write("\nThe correct answer is: 12a - 16b = 30")
    print("Question 3: " + "\nExpand and simplify: (x + 4)(x + 9)")
    f.write("\n\nQuestion 3: Expand and simplify: (x + 4)(x + 9)")
    answer3 = input()
    f.write("\n" + str(answer3))
    empty_line()
    if answer3 == 'x^2 + 13x + 45':
        score = score + 1
        f.write("\nCorrect")
    else:
        score = score
        f.write("\nIncorrect")
        f.write("\nThe correct answer is: x^2 + 13x + 45")
    print("Question 4: " + "Solve the simultaneous equation \n3x + y = 11 \n2x + y = 8")
    f.write("\n\nQuestion 4: " + "Solve the simultaneous equation \n3x + y = 11 \n2x + y = 8")
    answerX = input("x = ")
    answerY = input("y = ")
    answer4 = str(answerX) + str(answerY)
    empty_line()
    f.write("\nx = " + str(answerX) + "\ny = " + str(answerY))
    if answer4 == '34':
        score = score + 1
        f.write("\nCorrect")
    else:
        score = score
        f.write("\nIncorrect")
        f.write("\nThe correct answer is: \nx = 3 \ny = 4")
    print("Question 5: " + "Solve 9 - m = (8m + 5) / 3")
    f.write("\n\nQuestion 5: " + "Solve 9 - m = (8m + 5) / 3")
    answer5 = input("m = ")
    f.write("\nm = " + str(answer5))
    if answer5 == '2':
        score = score + 1
        f.write("\nCorrect")
    else:
        score = score
        f.write("\nIncorrect")
        f.write("\nThe correct answer is: m = 2")
    empty_line()
    str_score = str(score)
    print("Your score is: " + str_score + "/5")
    empty_line()
    f.write("\n\nYour score is: " + str_score + "/5")
    f.close()


# function where user can input a word
# and receive information on the word selected using oxford dictionary API - Leandro
# Adapted into program by Suraj
def english_main():
    # Importing user name from dictionary - Suraj
    name = user_data['name']
    app_id = "4b11e51d"
    app_key = "2f0e4476e477e029212ade1463481b90"
    # loop for user input
    while True:
        choose = input("Do you want to write a word or a sentence?\n")
        while True:
            if "word" in choose:
                word_id = input("\nEnter a Word: \n")
                if word_id != "":
                    break
            elif "sent" in choose:
                word_id = input("\nEnter a Sentence: \n")
                if word_id != "":
                    break
            else:
                choose = input("\nSorry " + name + ", that is an invalid choice, please try again:" )

        # pulling oxford dictionay API
        endpoint = "entries"
        language = "en-gb"
        url = 'https://od-api.oxforddictionaries.com:443/api/v2/' + endpoint + '/' + language + '/' + word_id.lower()

        r = requests.get(url, headers={"app_id": "4b11e51d", "app_key": "2f0e4476e477e029212ade1463481b90"})

        oxford_dict = json.loads(json.dumps(r.json()))

        x = json.dumps(r.json())
        error = '{"error": "No entry found matching supplied source_lang, word and provided filters"}'
        error_array = "['the nineteenth letter of the alphabet.']"
        # Adapted below code to display in program to desired effect - Suraj
        if x != error:

            print("\n" + word_id + " belongs to the family of: " + oxford_dict["results"][0]["lexicalEntries"][0]["lexicalCategory"]["text"])
            print("\nThe definition of " + word_id + " is: ")
            definition = oxford_dict["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
            print(str(definition))
            choice = input("\nWould you like to see this word in a sentence?: ")
            if ("ye" in choice) or ("ok" in choice) or ("sure" in choice):
                print("\nExample: ")
                if len(word_id) == 1:
                    print("None")
                else:
                    print(oxford_dict["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["examples"][0]["text"] + "\n")
            else:
                print("\nOkay " + name + ", maybe next time!")
            break
        else:
            print("\nSorry, that word is not spelled correctly!")
    empty_line()


# Function created using weather API to make an intelligent comment to the user based on the weather - Suraj/Soroush
def weather_main():
    # Importing user location information into function from dictionary
    location = user_location['location']
    # Start of adapted code for API from: https://openweathermap.org/current 
    api_key = "7a23354318d9d429a7b41dd215826c42"
    link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7a23354318d9d429a7b41dd215826c42&units=metric'.format(
        location)

    # Calling the imported python packages to connect with API and communicate from web
    response = requests.get(link)
    data = json.loads(json.dumps(response.json()))

    # Pulling relevant information from API
    temperature = data['main']['temp']
    wind_velocity = data['wind']['speed']
    description = data['weather'][0]['description']
    error = "404", "city not found"

    if data == error:
        print("I haven't heard of that location before!")
        # end of adapted code from: https://openweathermap.org/current

    else:
        # Taking information from the API dictionary and using it to generate an intelligent response to the user based
        # on the weather in their location - Suraj
        if ('rain' in description):
            print("By the way, it's raining in " + location + " today, I recommended you take an umbrella!")
        elif temperature > 16 and temperature<21:
            print("It's quite warm in " + location + ". No need for a coat.")
        elif temperature>=21:
            print("It's warm outside today. Make sure you keep hydrated!")
        elif temperature>10 and temperature<=16:
            print("The weather in " + location + " isn't too bad today, maybe take a hoodie with you though!")
        elif temperature <= 10:
            print("Oh, it's less than 10 degress today, you should wrap up warm when you leave the house!")
        elif temperature <=4:
            print("It is very cold in " + location + "today, you should wrap up those layers so you do not get too cold. Expect ice!")
        else:
            return False
        empty_line()


def stores_main():
    location = user_location['location']
    api_key = "oNklsNMHwvGQKhObny3z2P4pqOyOk3tjRYSuXAxbMBC9xtyCdC83zhBSHRXJMMvue3h7GJ-G5yT1uK5wJy6uBF1CImm2sI4QjJ_1juOr0ZWOjZwogDrQ_jfGdtvBXXYx"
    headers = {'Authorization': 'Bearer %s' % api_key}

    afirmitiveList = ["yes", "Yes", "YES", "true", "True", "TRUE", "yeah", "Yeah", "YEAH", "ok", "Ok", "OK",
                      "Okay""okay", "OKAY", "T", "t", "y", "Y", "YES", "okie", "Okie", "OKIE", "sure", "Sure", "SURE",
                      "Yh", "yh", "YH"]
    negativeList = ["no", "No", "NO", "Nah", "nah", "NAH", "false", "False", "FALSE", "f", "F", "N", "n", "nope",
                    "Nope", "NOPE"]

    #process_stores_welcome()
    #url = 'https://api.yelp.com/v3/businesses/search'
    #parama = {'term'}
    #req = requests.get(url, params=parama)
    #parsed = json.loads(req.text)
    #terms = parsed['term']

    #question = input("\nWhat do you like doing?")
    #for word in question:
        #if word in terms:
            #user_term = word
            #print(user_term)

    # Asking the user whether or not the API would be of use to them through basic questions - Suraj
    decision = input("Are you planning on leaving the house today? ")
    if decision in negativeList:
        pass
        empty_line()
    else:
        print("\nWould you like me to suggest some places for you to go in " + location + "?")
        decision2 = input()
        if decision2 in negativeList:
            pass
            empty_line()
        else:
            print("\nOkay let me ask you some questions first.")
            parLocation = location
            # End of manipulation contribution by Suraj
            parTerm = input("\nWhat are you looking for?: ")
            parLimit = input("How many results?: ")
            open_now_answer = input("Would you like to search only opened stores?: ")

            if open_now_answer in afirmitiveList:
                parOpen_now = True
            elif open_now_answer in negativeList:
                parOpen_now = False
            else:
                parOpen_now = False
                print("Sorry, I could not understand that.")

            url = 'https://api.yelp.com/v3/businesses/search'
            params = {'term': parTerm, 'location': "United kingdom " + parLocation, 'limit': parLimit,
                      'locale': "en_GB",
                      'open_now': parOpen_now}
            req = requests.get(url, params=params, headers=headers)
            parsed = json.loads(req.text)

            # print(json.dumps(parsed, indent=4))
            print(" ")
            if "error" in parsed:
                print(parsed["error"]["description"])
                print(" ")
                print("Please try again.")
                print(" ")
                return True
            else:
                # print(parsed)
                # print("not inside")
                businesses = parsed["businesses"]

                for business in businesses:
                    print("Name:", business["name"])
                    print("Rating:", business["rating"])
                    print("Address:", " ".join(business["location"]["display_address"]))
                    print("Phone:", business["phone"])
                    print("\n")

                if len(businesses) < int(parLimit):
                    if len(businesses) == 0:
                        print("Sorry, I could not find any result for " + parTerm + ", please try again.")
                        print("")
                        return True
                    else:
                        print("I could only find " + str(len(businesses)) + " results for " + parTerm)
                        return False
                else:
                    print("I found " + str(len(businesses)) + " results for " + parTerm)
                    return False
                empty_line()


# Function to display result - Suraj
def display(result):
    return result


# Function to insert an empty line - Suraj
def empty_line():
    print("")


# Function to exit the program - Suraj
def user_exit():
    choice = input("Would you like to exit the conversation or return to the menu? ")
    if ('ye' in choice) or ('sure' in choice) or ('ok' in choice) or ('not' in choice):
        print("Let's get started then!")
        x = 1
        empty_line()
    elif ('no' in continuation) or ('na' in continuation):
        print("Okay " + name + ", maybe next time.")
        x = 1
        exit()
    exit()
