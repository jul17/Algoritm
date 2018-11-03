from counter import Counter


def Selection(list):
    L = len(list)
    for i in range(0, L - 1):
        min = i
        for j in range(i + 1, L):
            if list[j].rating > list[min].rating:
                min = j
            Counter.compare_count()
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
        Counter.exchange_count()
    return list
