class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def __repr__(self):
        return 'lol'

def get_info(*args):
    if not False in args:
        print(args[0], args[1], args[2])