# Algorithm :
# Step 1: Repeat Step 2 For i = 0 to N-1
# Step 2: Repeat For J = i + 1 to N - I
# Step 3: IF A[J] > A[i]
# SWAP A[J] and A[i]
# [END OF INNER LOOP]
# [END OF OUTER LOOP
# Step 4: EXIT
ll = [10, 9, 7, 101]
for i in range(0, len(ll)):
    for j in range(i + 1, len(ll)):
        if ll[j] < ll[i]:
            ll[i], ll[j] = ll[j], ll[i]

print(ll)
