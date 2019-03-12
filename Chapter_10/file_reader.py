# Object for the file is made
filename = 'pi_million_digits.txt'

# 6. Object that references file is opened and printed to the screen
# 7. Takes each line from the file and stores it in a list
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Only print the first 52 numbers and then put ... in replace of the rest    
#print(pi_string[:52] + "...")

# Count prints the string and shows how long the string is
#print(len(pi_string))


