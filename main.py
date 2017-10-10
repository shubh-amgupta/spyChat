from spy_details import spy #import spy details from other file
from steganography.steganography import Steganography #Encryption of messages using Images. Install module steganography
from datetime import datetime #Date time module

print ("Welcome to spy chat, " + spy['name'])

question = raw_input("Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)? : ") #spy['name'] - it is a dictonary


#startchat function to start a chat with attributes of paricular spy
def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True #To run a loop for displaying menu
    current_status_message = None

    while show_menu:
        menu_choice = int(raw_input("What do you want to do? \n1. Add a status update \n2. Add a friend\n3. Select a friend\n4. Send Message\n5. Read Message\n6. Close Application\n"))

        if menu_choice == 1:
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
            friends_len = add_friend()
        elif menu_choice == 3:
            select_friend()
        elif menu_choice == 4:
            send_message()
        elif menu_choice == 5:
            read_message()
        elif menu_choice == 6:
            show_menu = False #Exit menu


STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.'] #List of status messages


#addstatus function to manipulate status of a spy
def add_status(current_status_message):
    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message) #add new status to existing status's list

    #print list of already existing status messages
    elif default.upper() == 'Y':
        item_position = 1
        #for loop to display every item in a list. Usiing temporary variable (message in this case)
        for message in STATUS_MESSAGES:
            print str(item_position) + ". " + message
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages :"))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    return updated_status_message #return updated status


#register a new user other than default user
if question.lower() == "n":

    spy_salutation = raw_input("Should I call you Mister or Miss?: ") #Salutation for new user

    spy_name = raw_input("Your name is " + spy['salutation']) #Salutation for new user

    spy_name = spy['salutation'] + " " + spy_name

    print "Alright " + " " + spy_name + ". I'd like to know a little bit more about you before we proceed."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = int(raw_input("What is your age?")) #age for new user
    if 50 > spy_age > 12:
        spy_rating = raw_input("What is your rating?") #rating for new user
        if 4.5 < spy_rating:
            print 'Great ace!'
        elif spy_rating > 3.5 and spy_rating <= 4.5:
            print 'You are one of the good ones.'
        elif spy_rating >= 2.5 and spy_rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
    else:
        print 'Sorry you are not of the correct age to be a spy'

    spy_is_online = True
    print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + spy_rating + " Proud to have you onboard"

    start_chat(spy['name'], spy['age'], spy['rating'])

else:
    start_chat(spy['name'], spy['age'], spy['rating'])


friends = []


#addfriend function to add a new friend in frineds list
def add_friend():
    #new dictonary for every new friend addded
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    #friends Info
    new_friend['name'] = raw_input("Please add your friend's name: ")
    new_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    #return length of frineds list
    return len(friends)


#selectfriend to select a frined from friends list
def select_friend():

    item_number = 0
    #to traverse friends list
    for friend in friends:
        print '%d. %s' % ((item_number + 1), friend['name'])
        item_number = item_number + 1

    friend_choice = input("Choose from your friends")
    return friend_choice - 1


#sendmessage to send a encoded message in an image
def send_message():

    #select a friend to whom message is to be send
    friend_choice = select_friend()

    original_image = raw_input("What is the name of the image?") #image to be encoded (encoded.png)
    output_path = 'secret_image.jpg' #output image. Result
    text = raw_input("What do you want to say?") #Message you want to send encoded in image
    Steganography.encode(original_image, output_path, text) #inbuilt function of steganography encode()

    #newchat dictonary which notes timestamp of send message using datetime module
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"


def read_message():

    sender = select_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"