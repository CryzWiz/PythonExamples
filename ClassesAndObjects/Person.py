
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, name):
        self.name = name

    def get_name(self):
        return print(self.name)
