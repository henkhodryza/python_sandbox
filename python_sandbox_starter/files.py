# Python has functions for creating, reading, updating, and deleting files.
# open a file

myFlie = open('myfile.txt', 'w')


myFlie.write('I love python')
myFlie.write('I love javascrip')
myFlie.close()

myFlie = open('myfile.txt')
