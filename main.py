from spy_details import Spy, ChatMessage, spy, friends #import spy details from other file
from steganography.steganography import Steganography #Encryption of messages using Images. Install module steganography
from datetime import datetime #Date time module
import csv #CSV module to manipulate CSV files (Comma Seperated Values)


def load_friends():
    with open('friends_data.csv', 'rb') as friends_data:
        reader = csv.read(friends_data)

        for row in reader:
            spy = Spy(row[0], row[1], row[2], row[3])
            friends.append(spy)

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



#addfriend function to add a new friend in frineds list
def add_friend():
    #new dictonary for every new friend addded
    new_friend = Spy('', '', 0, 0.0)

    #friends Info
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = int(raw_input(new_friend.name + "\'s Age? "))
    new_friend.rating = float(raw_input(new_friend.name + "\'s Smart rating? "))

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 1:
        try:
            with open("friends.csv", 'ab') as friends_data:
                write = csv.writer(friends_data)
                write.writerow([new_friend.name, new_friend.salutation, new_friend.age, new_friend.rating])
        except:
            print 'File not available'
        friends.append(new_friend)
        print '\nNew Friend Name " %s " Age " %d " of Rating " %.2f " Added into Friend List.' % (new_friend.name, new_friend.age, new_friend.rating)

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

    # split text message to check any special message involved or not
    message = text.split(' ')
    # If a Smart send a message with special words such as SOS, SAVE ME etc. you should display an appropriate message
    cases = ['SOS', 'Help', 'HELP', 'SoS', 'ASAP', 'asap']
    for any in cases:
        if any in message:
            print "Immediate action required"

    #newchat dictonary which notes timestamp of send message using datetime module
    new_chat = ChatMessage(text, True)

    friends[friend_choice]['chats'].append(new_chat)
    print "Your secret message is ready!"


def read_message():

    sender = select_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text, False)

    friends[sender]['chats'].append(new_chat)
    print "Your secret message has been saved!"



print ("Welcome to spy chat, " + spy.name)

question = raw_input("Continue as " + spy.salutation + " " + spy.name + "(Y/N)? : ") #spy['name'] - it is a dictonary

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


#register a new user other than default user
if question.lower() == "n":

    new_user = Spy('', '', 0, 0.0)

    new_user.salutation = raw_input("Should I call you Mister or Miss?: ") #Salutation for new user

    new_user.name = raw_input("Your name is " + new_user.salutation) #Salutation for new user

    new_user.name = new_user.salutation + " " + new_user.name

    print "Alright " + " " + new_user.name + ". I'd like to know a little bit more about you before we proceed."

    new_user.age = 0
    new_user.rating = 0.0
    new_user.is_online = False

    new_user.age = int(raw_input("What is your age?")) #age for new user
    if 50 > new_user.age > 12:
        new_user.rating = float(raw_input("What is your rating?")) #rating for new user
        if 4.5 < new_user.rating:
            print 'Great ace!'
        elif new_user.rating > 3.5 and new_user.rating <= 4.5:
            print 'You are one of the good ones.'
        elif new_user.rating >= 2.5 and new_user.rating <= 3.5:
            print 'You can always do better'
        else:
            print 'We can always use somebody to help in the office.'
    else:
        print 'Sorry you are not of the correct age to be a spy. Authentication Failed.'
        exit()

    new_user.is_online = True
    print "Authentication complete. Welcome " + new_user.name + " age: " + str(new_user.age) + " and rating of: " + str(new_user.rating) + " Proud to have you onboard"

    start_chat(new_user.name, new_user.age, new_user.rating)

else:
    start_chat(spy.name, spy.age, spy.rating)
