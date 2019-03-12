import json

""" Refractor your code to make it cleaner, easier to understand, and easier
to extend; turning formulas and code snippets into seperate functions."""
def get_stored_username():
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
    
def greet_user():
    """Greet the User by name."""
    username = get_stored_username()
    print(username)
"""    try:"""
    validuser = input("Is this your username?")
"""    if validuser == 'yes':
#        print("Welcome back, " + username + "!")
#    else:
#        username = get_new_username()
#        print("We'll remember you when you come back, " + username + "!")"""

#greet_user()
