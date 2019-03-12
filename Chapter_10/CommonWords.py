firstFile = 'HeartOfDarkness.txt'
secondFile = 'PrideAndPrejudice.txt'

try:
    with open(firstFile, encoding='utf-8') as f_obj:
        firstContents = f_obj.read()
    with open(secondFile, encoding='utf-8') as f_obj:
        secondContents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry file not found."
    print(msg)

# Count the number of times a specific word appears in different texts
else:
    first = firstContents.count('the')
    second = secondContents.count('the')
# Catches all appearances of the word you're looking for, regardless of how
# it's formatted
    third = firstContents.lower().count('the')
    fourth = secondContents.lower().count('the')
    print(third)
    print(fourth)
