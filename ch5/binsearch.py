def binsearch(A: list, x: int) -> int:

    n = len(A)
    lo, hi = -1, n

    # 반복문 불변식 1: lo < hi
    # 반복문 불변식 2 : A[lo] < x <= A[hi]
    # 그러나 lo가 -1일때 A[lo] = A[n-1]
    
    while lo + 1 < hi:
        # 가운데 인덱스 
        mid = (int)((lo + hi)/2)

        if A[mid] < x:
            lo = mid
        else:
            hi = mid
    return hi

ret = binsearch([1,2,3,4],4)
