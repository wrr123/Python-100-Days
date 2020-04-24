class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'talk with {self.name}')


person1 = Person('Smith')
person1.talk()
