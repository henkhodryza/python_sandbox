# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class User:
    # construsto
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'


class customer(User):
    def __init__(self, balance):
        self.balance = balance


hendry = User('Hendry Khoza', 'test@123', 24)
print(hendry.greeting())
