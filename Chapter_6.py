# Creating a dictionary and print the values to the screen
alien_1 = {'color': 'green', 'points': 5}

print(alien_1['color'])
print(alien_1['points'])

# Accessing values in a dictionary
new_points = alien_1['points']
print("You just earned " + str(new_points) + " points!")
print("You just earned " + str(new_points) + " points!")

# Adding new values
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1)

# Starting with an empty dictionary
alien_0 = {}
alien_0['color'] = 'purple'
alien_0['points'] = 7
print (alien_0)

# Modifying values in a dictionary
alien_0['color'] = 'yellow'
print("Th alien color is now " + alien_0['color'] + ".")

# Bigger example of modifying values
alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_3['x_position']))

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3
    
alien_3['x_position'] = alien_3['x_position'] + x_increment

print("New x_position: " + str(alien_3['x_position']))

# Delete  key-value pairs. Permanently are deleted
del alien_0['points']
print(alien_0)

# A dictionary of similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',}
    
print("Jen's favorite language is " + 
    favorite_languages['sarah'].title() +
    ".")
# Looping through a dictionary


for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

friends = ['phil', 'sarah']

# Looping throug hall keys in a dictionary
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
    
# Looping through a dictionary keys in alphabetical order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all the values in a dictionary
print("\nThe followng languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Loop through the values without repeating any variables
for language in set(favorite_languages.values()):
    print("\n" + language.title())

# Nesting a list of dictionaries
predator_1 = {'color': 'green', 'points': 5}
predator_2 = {'color': 'yellow', 'points': 10}
predator_3 = {'color': 'red', 'points': 15}

predators = [predator_1, predator_2, predator_3]

for predator in predators:
    print(predator)

# Nesting an empty dictionary
soldiers = []

for soldier_number in range(30):
    new_soldier = {'color': 'green', 'points': 5, 'speed': 'slow'}
    soldiers.append(new_soldier)

for soldier in soldiers[0:3]:
    if soldier['color'] == 'green':
        soldier['color'] = 'yellow'
        soldier['speed'] = 'medium'
        soldier['points'] = 10

for soldier in soldiers[:5]:
    print(soldier)
print("...")

print("Total number of soldiers: " + str(len(soldiers)))

# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# Using a dictionary within a dictionary
users = { 
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
        'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

