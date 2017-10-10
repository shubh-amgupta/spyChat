
from spy_details import spy

print ("Welcome to spy chat, " + spy['name'])

question = raw_input("Continue as " + spy['salutation'] + " " + spy['name'] + "(Y/N)? : ")

def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    current_status_message = None

    while show_menu:
        menu_choices = input("What do you want to do? \n1. Add a status update \n2. Close Application\n")
        menu_choice = input(menu_choices)

        if menu_choice == 1:
            current_status_message = add_status(current_status_message)
        elif menu_choice == 2:
            show_menu = False



STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.']

def add_status(current_status_message):
    if current_status_message is not None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            STATUS_MESSAGES.append(updated_status_message)

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:
            print item_position + ". " + message
            item_position = item_position + 1

        message_selection = input("\nChoose from the above messages :")

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    return updated_status_message

if question.lower() == "n":

    spy['salutation'] = raw_input("Should I call you Mister or Miss?: ")

    spy_name = raw_input("Your name is " + spy['salutation'])

    spy_name = spy['salutation'] + " " + spy_name

    print "Alright " + " " + spy_name + ". I'd like to know a little bit more about you before we proceed."

    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_age = int(raw_input("What is your age?"))
    if 50 > spy_age > 12:
        spy_rating = raw_input("What is your rating?")
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
    print "Authentication complete. Welcome " + spy_name + " age: " + str(
        spy_age) + " and rating of: " + spy_rating + " Proud to have you onboard"

    start_chat(spy['name'], spy['age'], spy['rating'])

else:
    start_chat(spy['name'], spy['age'], spy['rating'])
    
friends = []

def add_friend():
    new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }

    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")
    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")
    new_friend['rating'] = input("Spy rating?")

    if len(new_friend['name']) > 0 and new_friend['age'] > 12 and new_friend['rating'] >= spy['rating']:
        friends.append(new_friend)
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)

def select_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s' % ((item_number + 1), friend['name'])
        item_number = item_number + 1
