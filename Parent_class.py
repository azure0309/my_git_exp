class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'

    def __repr__(self):
        return 'lol'

me = Person('Nandia', 23)
print(me, end='-')

def get_info(name, age, gender):
    print(name, age, gender)