#spy = {
#  'name': 'SuperMan',
#  'salutation': 'Mr.',
#  'age': 27,
#  'rating': 4.9,
#  'is_online': True,
#  'chats': []
#}
from datetime import datetime

class Spy:

  def __init__(self, name, salutation, age, rating):
    self.name = name
    self.salutation = salutation
    self.age = age
    self.rating = rating
    self.is_online = True
    self.chats = []
    self.current_status_message = None

#defaultUser
spy = Spy('SuperMan', 'Mr.', 27, 4.7)

#friends list
#friend_one = Spy('Batman', 'Mr.', 25, 4.9)
#friend_two = Spy('Flash', 'Mr.', 22, 4.5)
#friend_three = Spy('Wonder Women', 'Ms.', 26, 4.8)

#friends = [friend_one, friend_two, friend_three]
friends = []

class ChatMessage:

  def __init__(self, message, sent_by_me):
    self.message = message
    self.time = datetime.now()
    self.sent_by_me = sent_by_me