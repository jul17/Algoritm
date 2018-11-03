class Student:

    def __init__(self, name, surname, rating, height):
        self.name = name
        self.surname = surname
        self.rating = rating
        self.height = height

    def __repr__(self):
        return str(self.name) + " " + str(self.surname) + " " + str(self.rating) + " " + str(self.height)
