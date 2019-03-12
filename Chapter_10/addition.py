import math
while True:
# Allows user to input values to be added together
    try:
        first_number = input ("Enter the first number: ")
        if first_number == 'q':
            break
        second_number = input ("\nEnter the second number: ")
        if second_number == 'q':
            break
        addition = int(first_number) + int(second_number)
        
# Handles any errors that are not integers
    except Exception as x:
        print("Get your shit together!")
    else:
        print(addition)    
    
    
