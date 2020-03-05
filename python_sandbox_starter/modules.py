# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
# core modules
from validator import validate_email
from camelcase import CamelCase
from datetime import date
from time import time
today = date.today()

# pip Module

c = CamelCase()
# print(c.hump('Hello beautiful world'))

# customee module


email = 'test#test.com'

if validate_email(email):
    print('Email is valid')
else:
    print('your email is bad')
