"""This is where the process functions are created for the chatbot"""


# Creating empty user list
user = []
# creating empty user dictionary
user_data = {}

# function to display chatbot welcome message
def process_welcome_message():
    print("Hello, my name is ChatBot!")


# function to add user name to user dictionary, to use throughout program
def process_user_name(u_name):
    user_data['name'] = u_name
    user.append(user_data)


# function for the user to select what option they would like to select
def process_user_option():
    print("I am here to help you with either Maths, English, weather or restaurants information!")
    print("Selecting option 1 will allow me to help you with GCSE algebraic Maths.")
    print("Selecting option 2 will allow me to help you with English definitions.")
    print("Selecting option 3 will allow me to provide you with weather information.")
    print("Selecting option 4 will allow me to provide you with restaurants information.")

def process_maths_welcome():
    print("You have selected Maths! My aim is to teach you the basic principles of GCSE algebra.")
    print("I will also create a schedule for you based on when your exams are.")
    print("Shall we get started? ")


def process_english_welcome():
    print("You have selected English. My aim is supply you with definitions to any English words.")
    print("Shall we get started? ")


def process_maths_question():
    print("First we will test your basic algebra.")
    print("Can you give me the answer to 2a + 6 = 10?")


# process for giving comment about the weather to the user
def process_weather_welcome():
    print("You have selected the weather option. My aim is to provide you with the relevant weather information for your chosen location")
    print("Shall we get started? ")
    
    
def process_stores_welcome():
    print("You have selected the stores searching option. My aim is to provide you with the relevant information about stores for your chosen location")
    print("Shall we get started? ")
    
    


