# wiki: https://en.wikipedia.org/wiki/Insertion_sort
# 插入算法， 同打牌
ll = [10, 9, 7, 101]
# work left to right
for i in range(1, len(ll)):
    # 需要插入的牌，当前需要换位置的牌
    temp = ll[i]
    # j永远都是需要插入的牌应该插入的位置
    j = i - 1
    # each item 对从right 到 left对比， 如果需要插入的牌 < 对比的牌，那么对比的牌往后挪一个位置，
    while j >= 0 and temp <= ll[j]:
        # 大的往后挪一个位置
        ll[j + 1] = ll[j]
        # 对比位置，也就是插入位置的前一个位置
        j = j - 1
    # 如果插入的牌>对比的牌， 那么插入对比的牌后面即可
    ll[j + 1] = temp
print(ll)
