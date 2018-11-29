from printer import Printer
from Read import Reader
from timeit import default_timer as timer


class Sort:
    def __init__(self):
        self.comparanceCount = 0
        self.swap = 0

    def quick_sort(self, array):
        if (len(array) <= 1):
            self.comparanceCount += 1
            return array
        else:
            self.comparanceCount += 1
            array_big = [];
            array_small = []
            pivot = array[len(array) - 1]
            for i in range(0, len(array) - 1):
                if (array[i].price >= pivot.price):
                    self.swap += 1
                    array_big.append(array[i])
                else:
                    self.swap += 1
                    array_small.append(array[i])
            return self.quick_sort(array_small) + [pivot] + self.quick_sort(array_big)

    def bubble_sort(self, array):
        no_sorted = True
        while (no_sorted):
            for i in range(0, len(array) - 2):
                self.comparanceCount += 1
                if (array[i].speed < array[i + 1].speed):
                    no_sorted = True
                    self.swap += 1
                    var = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = var
            no_sorted = False
        return array


if __name__ == '__main__':
    read = Reader()

    array = [Printer("Canon", 5, 6000), Printer("Canon", 8, 9000), Printer("HP", 2, 3000), Printer("HP", 7, 6500),
             Printer("HP", 2, 2000)]
    array = read.read()
    print()
    print("Sorted by price")
    start = timer()
    sort = Sort()
    result = sort.quick_sort(array)
    end = timer()
    for i in result:
        i.print_printer()
    print("Swap=" + str(sort.swap))
    print("Compier=" + str(sort.comparanceCount))
    print("Time=" + str(end - start))
    sort = Sort()
    start = timer()
    result = sort.bubble_sort(array)
    end = timer()
    print("Sorted by speed")
    for i in result:
        i.print_printer()
    print("Swap=" + str(sort.swap))
    print("Compier=" + str(sort.comparanceCount))
    print("Time=" + str(end - start))
