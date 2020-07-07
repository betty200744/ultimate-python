def smallest(arr, i):
    small = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[small]:
            small = j
    return small


arr = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]

for i in range(0, len(arr)):
    small = smallest(arr, i)
    arr[small], arr[i] = arr[i], arr[small]

print(arr)
