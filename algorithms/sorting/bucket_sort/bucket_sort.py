# 桶排序， 或者分类排序
# https://www.javatpoint.com/bucket-sort
# wiki： https://en.wikipedia.org/wiki/Bucket_sort
# Algorithm
# Step 1 START
# Step 2 Set up an array of initially empty "buckets".
# Step 3 Scatter: Go over the original array, putting each object in its bucket.
# Step 4 Sort each non-empty bucket.
# Step 5 Gather: Visit the buckets in order and put all elements back into the original array.
# Step 6 STOP
DEFAULT_BUCKET_SIZE = 5
ll = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]


def insertion(ll):
    for i in range(1, len(ll)):
        temp = ll[i]
        j = i - 1
        while j >= 0 and temp <= ll[j]:
            ll[j + 1] = ll[j]
            j -= 1
        ll[j + 1] = temp
    return ll


def bucket_sort(ll):
    arr = []
    bucket_num = 5
    # 创建n个桶，初始化值
    for i in range(bucket_num):
        arr.append([])
    # Put array elements in different buckets
    for j in ll:
        index_bucket = int(bucket_num * j)
        print(index_bucket)
        arr[index_bucket].append(j)
    # Sort individual buckets
    for i in range(bucket_num):
        arr[i] = insertion(arr[i])
    # concatenate the result
    k = 0
    for i in range(bucket_num):
        for j in range(len(arr[i])):
            ll[k] = arr[i][j]
            k += 1
    return ll


print(bucket_sort(ll))
