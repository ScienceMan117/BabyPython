# Using If statements in a For loop
cars = ['mazda', 'toyota', 'nissan', 'tesla', 'chevrolet']

for car in cars:
    if car == 'nissan':
        print(car.upper())
    else:
        print(car.title())


# Checking the variable to see if it isn't a specific string
requested_car = 'Volt'

if requested_car != 'volt':
    print ('\n' + "About fucking time.")


# Checking to see if a number is in an array
numbers = [1, 12, 69, 101,]
numero = 7

if numero not in numbers:
    print(numero)

# Using else-if statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else: 
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# The if-elif-else Chain
age = 12

if age < 4:
    print("Your admisssion cost is $0")
elif age < 18:
    print("Your admission cosdt is $5")
else:
    print("Your admission cost is $10")

#Another if-elseif chain
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")

# -Don't need to include else in the statement, and you can use as many elif
# statements as you would like
#- If your are doing a short block of code use if-elif-else statement, but if 
# then use a series of If statements

# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping+ ".")
print("\nFinished making your pizza!")

# A list without any elements can be checked (pg. 91)

# Using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else: 
        print("Sorry, we don't have " + requested_topping + ".")
        
        
print("\nFinished making your pizza!")
