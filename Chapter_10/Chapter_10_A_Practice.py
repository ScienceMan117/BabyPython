# Reading in the entire file and printing
with open('I_Learned.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
filename = 'I_Learned.txt'

# Looping over the file object and printing
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines in a list and then working with them outside the with block
with open(filename) as file_object:
    lines = file_object.readlines()

learn_string = ''
for line in lines:
    learn_string += line.strip()

# Replace the word Python in learn_string object to C++
print(learn_string.replace('Python', 'C++'))
