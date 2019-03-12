print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# Take two inputted numbers divide them and output an error message without the
# code breaking if the code division operation does not work
while True:
    first_number = input ("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:        
        answer = int(first_number) / int(second_number)
    except ZeroDivision:
        print("You can't divide by 0!")
    else:
        print(answer)
