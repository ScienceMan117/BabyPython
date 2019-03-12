# Setting the contents 
filename = 'alice.txt'

# Try block that includes only the code that might cause an error.
try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
        
# Explains how to respond to an error message if the Try Block doesn't work
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
    
# If the operation is successful the Else Block performs an action
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
