# Passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
       msg = "Hello, " + name.title() + "!"
       print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
    
### Modifiying a list Pg.147-148
#Start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left
#Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
    
#Simulate creating a 3D print from the design
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


### Passing an Arbitrary Number of Arguments Pg. 151
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza")

make_pizza('pepperono')
make_pizza('mushroms', 'green peppers', 'extra cheese')

### Mixing Positional and Arbitrary Arguments Pg. 152
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

### Using arbitrary keyword arguments
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
    
user_profile = build_profile('albert', 'einstein', location='printeon',
                            field='physics')
print(user_profile)

###Storing your functions in Modules. Importing an Entire Module
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " +str(size)+ "-inch pizza with the following toppings:")
    for topping in toppings:
            print("- " + topping)

### Using as to Give a function an Alias
#from pizza import make_pizza as mp

#mp(16, 'pepperoni')
#mp(12, 'mushrooms', 'green peppers', 'extra cheese')

### LEARN MORE ABOUT MODULES
