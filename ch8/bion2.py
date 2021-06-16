cache = [[-1]*30]*30


def bino2(n: int, r: int) -> int:
    # 기저 사례
    if r == 0 or n == r:
        return 1
    if cache[n][r] != -1:
        return cache[n][r]
    return bino2(n-1, r-1) + bino2(n-1, r)

print(bino2(4,2))
    