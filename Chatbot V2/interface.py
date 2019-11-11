"""To accept user inputs from the keyboard"""

from process import process_welcome_message, process_user_name, process_user_option
from process import user_data, process_maths_welcome, process_english_welcome, process_maths_question, process_stores_welcome
from process import process_weather_welcome
from data import read_user, user
import requests
import json
from dictionary import convo_words, keywords

choice = {}


# Function to display welcome message and take user name as input
def user_name():
    process_welcome_message()
    empty_line()
    name = input("What is your name? ")
    empty_line()
    process_user_name(name)
    print("Hello " + name)


def user_feeling():
    name = user_data['name']
    feeling = input("How are you today? ").lower()
    sentence = feeling.split()
    empty_line()
    for word in sentence:
        if word in convo_words:
            data = convo_words.get(word, "")
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
    for secondary in sentence:
        if secondary in keywords:
            data = keywords.get(secondary, "")
            if data == 1:
                print("I am great, and excited to help you, thank you for asking!")
                empty_line()
                break
            else:
                continue
    #process_weather_welcome()
    #if feeling not in convo_words:
        #print("Hmmm, i have't heard that response before! I will remember that response from now on " + name)
        #convo_words['feeling'] = 1
        #empty_line()


def user_option():
    name = user_data['name']
    x = 0
    process_user_option()
    while x < 1:
        selection = input("Please select either option 1, 2, 3 or 4: ")
        empty_line()
        choice['selection'] = selection
        user.append(choice)
        selectionInt = int(selection)
        if (selectionInt > 0) and (selectionInt < 5):
            x = 1
        else:
            print("I'm sorry " + name + ", that is an invalid option! Please try again")
            empty_line()
            x = 0


def selection():
    x = 0
    name = user_data['name']
    decision = choice['selection']
    decision = int(decision)
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
                print("Sorry " + name + ", that is not a valid selection, please try again!")
                x = 0

    elif decision == 3:
        process_weather_welcome()
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
                print("Sorry " + name + ", that is not a valid selection, please try again!")
                x = 0
    
    elif decision ==  4:
        process_stores_welcome()
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
                print("Sorry " + name + ", that is not a valid selection, please try again!")
                x = 0
    

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



# function where user can input a word and recieve information on the word selected
def english_main():
    name = user_data['name']
    app_id = "4b11e51d"
    app_key = "2f0e4476e477e029212ade1463481b90"
    # loop for user input
    while True:
        choose = input("\nDo you want to write a word or a sentence?\n")
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

def weather_main():
    user_city = input("Please enter your city:")
    api_key = "7a23354318d9d429a7b41dd215826c42"
    link = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=7a23354318d9d429a7b41dd215826c42&units=metric'.format(
        user_city)

    response = requests.get(link)
    data = json.loads(json.dumps(response.json()))

    temperature = data['main']['temp']
    wind_velocity = data['wind']['speed']
    description = data['weather'][0]['description']
    error = "404", "city not found"

    if data == error:
        print("I'm sorry, I cannot provide the weather for " + user_city)

    else:
        print("The temperature in " + user_city, "is: {} degree Celsius".format(temperature))
        print("The wind speed in " + user_city, "is: {} m/s".format(wind_velocity))
        print("The weather in " + user_city, "can be described as: {}".format(description))
        if 'rain' in description:
            print("It's recommended to bring an umbrella!")
            
            
def stores_main():
    api_key="oNklsNMHwvGQKhObny3z2P4pqOyOk3tjRYSuXAxbMBC9xtyCdC83zhBSHRXJMMvue3h7GJ-G5yT1uK5wJy6uBF1CImm2sI4QjJ_1juOr0ZWOjZwogDrQ_jfGdtvBXXYx"
    headers = {'Authorization': 'Bearer %s' % api_key}

    parLocation = input("Please enter your city: ")
    parTerm = input("What are you looking for?: ")
    parLimit = input("How many results?: ")
    open_now_answer = input("Would you like to search only opened stores?(T/F): ")

    afirmitiveList = ["yes","Yes","YES","true","True","TRUE","yeah","Yeah","YEAH","ok","Ok","OK","Okay""okay","OKAY","T","t","y","Y","YES","okie","Okie","OKIE","sure","Sure","SURE","Yh","yh","YH"]
    negativeList = ["no","No","NO","Nah","nah","NAH","false","False","FALSE","f","F","N","n","nope","Nope","NOPE"]
    
    if open_now_answer in afirmitiveList:
        parOpen_now = True
    elif open_now_answer in negativeList:
        parOpen_now = False
    else:
        parOpen_now = False
        print("Sorry, I could not understand that, I asume that the answers is no.")


    url='https://api.yelp.com/v3/businesses/search'
    params={'term': parTerm, 'location':"United kingdom " + parLocation, 'limit': parLimit, 'locale':"en_GB", 'open_now':parOpen_now}
    req = requests.get(url, params=params, headers=headers)
    parsed = json.loads(req.text)
        #print(json.dumps(parsed, indent=4))
    print(" ")
    if "error" in parsed :
        print(parsed["error"]["description"])
        print(" ")
        print("Please try again.")
        print(" ")
        return True
    else :
        #print(parsed)
        #print("not inside")
        businesses = parsed["businesses"]

        for business in businesses:
            print("Name:", business["name"])
            print("Rating:", business["rating"])
            print("Address:", " ".join(business["location"]["display_address"]))
            print("Phone:", business["phone"])
            print("\n")

    
        if len(businesses) < int(parLimit):
            if len(businesses)==0:
                print ("Sorry, I could not find any result for " + parTerm + ", please try again.")
                print("")
                return True
            else:
                print ("I could only find " + str(len(businesses)) + " results for " + parTerm)
                return False
        else:
            print("I found " + str(len(businesses)) + " results for " + parTerm)
            return False






# Function to display result
def display(result):
    return result

def empty_line():
    print("")
