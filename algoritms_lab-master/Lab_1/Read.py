from printer import Printer


class Reader:
    def __init__(self):
        NAME = 0
        SPEED = 1;
        PRICE = 2

    def read(self):
        file = open("printer_input_data.csv", "r")
        array = []
        for i in file:
            lib = i.split(",")
            array.append(Printer(str(lib[self.NAME]), int(lib[self.SPEED]), int(lib[self.PRICE])))
        return array
