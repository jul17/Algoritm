class Printer:
    def __init__(self, name, speed, price):
        self.name = name
        self.speed = speed
        self.price = price

    def print_printer(self):
        print("Name: " + str(self.name) + " , Price " + str(self.price) + " , Speed " + str(+self.speed))
