# wiki:https://en.wikipedia.org/wiki/Shellsort
# geeksforgeeks:https://www.geeksforgeeks.org/shellsort/
# In practice the gap sequence could be anything, but the last gap is always 1 to finish the sort.


def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2


arr = [701, 301, 132, 57, 23, 10, 4, 1]
shellSort(arr)
print(arr)
