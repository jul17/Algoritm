from counter import Counter

def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j].height <= pivot.height:
            i = i + 1

            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        Counter.compare_count()
    Counter.exchange_count()
    temp = arr[i + 1]
    arr[i+1] = arr[high]
    arr[high] = temp
    Counter.exchange_count()
    return(i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def quickS(list):
    l = len(list)
    quickSort(list, 0, l-1)
    return list
















