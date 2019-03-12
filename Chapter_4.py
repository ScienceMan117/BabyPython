teams = ['seahawks', 'eagles', 'raiders']

# Using For loops
for teams in teams:
   # print(teams)
    print(teams.title() + ", is my favorite NFL football team!")
    print("I want to see the " + teams.title() + " make it to the Superbowl." +
        ".\n")
#INDENTING IS IMPORTANT! Next element used in the array will be the last item
print("But Most of all I want to see the " + teams.title() + " win." + ".\n")

# using range of numbers
models = list(range(101, 120))
print(models)

# using range and increments (start number, end number, increments)
model = list(range(101,120,3))
print(model)

# How to put numbers into an array using the For and Range function
numbers = []
for value in range(1, 10):
    #num = value / 2
    #numbers.append(num)
    #OR make it like this!
    numbers.append(value / 2)
# Displaying min, max and sum    
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(numbers)

# Generate elements to put into an array
corners = [value**3 for value in range(1,11)]
print(corners)

#Slicing a list(specifing the list of the first and last elements)
players = ['lynch', 'russel', 'brady', 'jones']
#print(players[1:4])
#print(players[0:2])
#print(players[2:])
#print(players[-2:]) 
print("Here are some awesome players: " + ".\n")

# Looping through a slice
for players in players[:3]:
    print(players.title())

my_beverages = ['juice', 'alcohol', 'water', 'maple syrup']
weekends = my_beverages[:]

print("My favorite beverages are:")
print(my_beverages)

print("\nMy friend's favorite drinks are: ")
print(weekends)

#Can seperate lists, even if one list is based on another (pg.67). MUST include
# ( : ) to copy over lists, or otherwise list2 will be an exact replicate of 
#list 1


# How to use a tuple, aka an immutable list
dimensions = (200, 50)
for dimensions in dimensions:
    print(dimensions)
# Can redefine tuples, the same way you made them


