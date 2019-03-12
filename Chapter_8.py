# Passing Information to a Function
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')

# Positional Arguments & Multi-Function Calls. Order matters
def describe_pet(animal_type, pet_name):
    """Display a simple greeting."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Returning a Simple Value
#def get_formatted_name(first_name, last_name):
#    """Return a full name, neatly formatted."""
#    full_name = first_name + ' ' + last_name
#    return full_name.title()

#musician = get_formatted_name('jimi', 'hendrix')
#print(musician)

# Making an argument Optional
def get_formatted_name(first_name, middle_name, last_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print (musician)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
