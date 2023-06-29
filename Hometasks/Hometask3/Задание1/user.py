class User:


    def __init__(self, name, surname):
        self.first_name = name
        self.second_name = surname

    def sayName(self):
        print("My name is", self.first_name,)

    def saySurname(self):
        print("My surname is", self.second_name)

    def sayFullName(self):
        print("My full name is", self.first_name, self.second_name)
    




