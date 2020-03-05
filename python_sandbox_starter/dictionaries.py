# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create Dictionary

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# get value
print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555 555 555'

print(person)

person2 = person.copy()
person2['city'] = 'Boston'

del(person['age'])
person.pop('phone')


# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
