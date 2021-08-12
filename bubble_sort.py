unsorted = [52, 27, 91, 18, 71, 33, 55, 44, 109]
n = len(unsorted)


def bubble(unsorted):
    for i in range(n):
        for j in range(n-i-1):
            if unsorted[j] > unsorted[j+1]:
                buff = unsorted[j]
                unsorted[j] = unsorted[j+1]
                unsorted[j+1] = buff

print(unsorted)
bubble(unsorted)
print(unsorted)
