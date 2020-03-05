# A List is a collection which is ordered and changeable. Allows duplicate members.


# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# get a value
print(fruits[1])

# get the length of an array
print(len(fruits))

# Append to list
print(fruits.append('Mangos'))

fruits.remove('Grapes')

fruits.insert(2, 'strawberries')
