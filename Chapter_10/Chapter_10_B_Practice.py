filename = 'guest.txt'
name = ''
reason = ''
while name != 'quit':
    name = input("Please write your first and last name: ")
    if name != 'quit':
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
            if name != 'quit':
                print("Welcome " + name)
            while reason != 'quit':
                reason = input("Why do you like programming?")
                if reason != 'quit':
                    file_object.write(reason + "\n")
            reason = ''
