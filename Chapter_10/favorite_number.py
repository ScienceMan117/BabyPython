import json

def get_stored_number():
    filename = 'numbers.json'
    try:
        with open(filename) as f_obj:
            usernumber = json.load(f_obj)
    except FileNotFoundError:
        return None
    else: return usernumber
    
def get_new_usernumber():
    usernumber = input("What is your favorite number? ")
    filename = 'numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(usernumber, f_obj)
    return usernumber

def print_number():
    usernumber = get_stored_number()
    if usernumber:
        print("I know your favorite number! It's " + usernumber + "!")
    else:
        usernumber = get_new_usernumber()
        print("I know your favorite number! It's " + usernumber + "!")

print_number()
