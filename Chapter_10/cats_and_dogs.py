firstFileName = 'cats.txt'
secondFileName = 'dogs.txt'

try:
    with open(firstFileName, encoding='utf-8') as f_obj:
        firstContents = f_obj.read()
    with open(secondFileName, encoding='utf-8') as f_obj:
        secondContents = f_obj.read()

except FileNotFoundError:
#    msg = "Sorry but one of the files does not exist"
#    print(msg)
     pass
     
else:
    print(firstContents)
    print(secondContents)
