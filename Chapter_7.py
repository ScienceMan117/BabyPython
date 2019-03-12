# Input something and have it repeated back to you
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

# Prompt the user for their name and then personalize the message.
#prompt = "If you tell us who you, we can personalize the messages you see."
#prompt+= "\nWhat is your first name? "

#name = input(prompt)
#print("\nHello, " + name + "!")

# Inputing integers
#height = input("How tall are you? ")
#height = int(height)

#if height >= 36:
#    print("\nYou're tall enough to ride!")
#else:
#    print("\nYou'll be able to ride when you're a little older.")

# Using Modulators
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)

#if number % 2 == 0:
#    print("\nThe number " + str(number) + " is even.")
#else:
#    print("\nThe number " + str(number) + " is odd.")

# While loop in Action
#current_number = 1
#while current_number <= 5
#    print(current_number)
#    current_number += 1

# Letting the User Choose when to quit    
#prompt = "\nTell me something, and I will repeat it back to you."
#prompt += "\nEnter 'quit' to end the program."

#message = ""
#while message != 'quit':
#    message = input(prompt)
#    print(message)

# Using a Flag
#prompt = "\nTell me something, and I will repeat it back to you: "
#prompt +="\nEnter 'quit' to end the program."

#active = True
#while active:
#    message = input(prompt)
    
#    if message == 'quit':
#        active = False
#    else: 
#        print(message)

# Using break to Exit a loop
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\(Enter 'quit' when you are finished.) "

#while True: 
#    city = input(prompt)
    
#    if city == 'quit':
#        break
#    else:
#        print("I'd love to go to " + city.title() + "!")


# Using continue in a loop
#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue
    
#    print(current_number)

# Moving Items from one list to another
unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Filling a Dictionary with User Input

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

