"""This is where the process functions are created for the chatbot"""

from data import user, location

# creating empty user dictionary - Suraj
user_data = {}

# creating user location dictionary - Suraj
user_location = {}

# function to display chatbot welcome message - Suraj
def process_welcome_message():
    print("Hello, my name is ChatBot!")


# function to add user name to user dictionary, to use throughout program - Suraj
def process_user_name(u_name):
    user_data['name'] = u_name
    user.append(user_data)

# Function to store user location in dictionary - Suraj
def process_user_location(u_location):
    user_location['location'] = u_location
    user.append(user_location)


# function for the user to select what option they would like to select - Suraj
def process_user_option():
    print("I am here to help you with either Maths or English!")
    print("Selecting option 1 will allow me to help you with GCSE algebraic Maths.")
    print("Selecting option 2 will allow me to help you with English definitions.")
    print("Selecting option 3 will terminate the conversation.")

# Below 4 functions are simple print statements - Suraj
def process_maths_welcome():
    print("You have selected Maths! My aim is to teach you the basic principles of GCSE algebra.")
    print("Shall we get started? ")


def process_english_welcome():
    print("You have selected English. My aim is supply you with definitions to any English words.")
    print("Shall we get started? ")


def process_maths_question():
    print("First we will test your basic algebra.")
    print("Can you give me the answer to 2a + 6 = 10?")


def process_stores_welcome():
    print("Are you planning to leave the house today?")



