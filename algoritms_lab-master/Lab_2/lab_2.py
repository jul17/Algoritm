class Calendar:

    def __init__(self, array):
        self.array = array

    def quick_sort(self, array):
        if (len(array) <= 1):
            return array
        else:
            array_big = [];
            array_small = []
            pivot = array[len(array) - 1]
            for i in range(0, len(array) - 1):
                if (array[i][0] >= pivot[0]):
                    array_big.append(array[i])
                else:
                    array_small.append(array[i])
            return self.quick_sort(array_small) + [pivot] + self.quick_sort(array_big)

    def changing_calendar(self):
        self.result = []
        i = 0
        while i < len(self.array):
            start = self.array[i][0]
            end = self.array[i][1]
            k = i + 1
            flag = True
            while k < len(self.array) and flag == True:
                if (self.array[i][1] < self.array[k][0]):
                    i = k - 1
                    flag = False
                else:
                    if (end < self.array[k][1]):
                        end = self.array[k][1]
                    if (k == len(self.array) - 1):
                        i = k
                        flag = False
                    else:
                        k += 1
            self.result.append((start, end))
            i += 1
