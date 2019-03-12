print("Hello Python World!")

cats = ['maincoons', 'Ragdolls', 'Persians', 'Russian Blues']
message = "My FAVORITE type of cat are " + cats[0].title() + "."

print(message)

cats[2] = 'Hairless'
#print(cats)

# Add an item at the end of the list
cats.append('Savanah')
#print(cats)

dogs = []

dogs.append('Poodle')
dogs.append('Retriever')
dogs.append('Pitbull')

#Inserting an element into a specific part of the list
dogs.insert(2, 'Foundlands')

#Deleting an element from the list 
del dogs[0]
#print(dogs)

#remove an item in the list but  be able to use it later (default is last item)
popped_cats = cats.pop(2)
#print(cats)
#print(popped_cats)

# Removing an item by value
decent = 'Ragdolls'
cats.remove(decent)
# print ("\nA " + decent.title() + "Is almost as good as " + cats[0])

#Sorting a List
# print(dogs)
dogs.sort()
print(dogs)
dogs.sort(reverse=True)
print(dogs)

# Get the number of elements in the list
num = len(dogs)
print (num)


