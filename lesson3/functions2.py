import functions
# from functions import hello
from functions import hello as hello2
from lesson1.types_1 import names


def hello(name, last_name):
    print('Hello 1' + ' ' + name + ' ' + last_name)


functions.hello('Ali', 'Rn')
# print(functions.age)

hello('Ali', 'Rn')

hello2('Ali', 'Rn', 'Good Byeeeee')

print(names)
