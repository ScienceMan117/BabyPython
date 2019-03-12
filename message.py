filename = 'programming.txt'

# Opening the file and setting the file to write mode
# Can also use 'r' (read), 'a' (append), and 'r+' to read and write into the file
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
