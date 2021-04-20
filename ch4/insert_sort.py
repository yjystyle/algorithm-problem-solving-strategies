def insert_sort(A):
    for i in range(len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j = j-1
    return A


ret = insert_sort([100, 91, 90, 92])
print(ret)
