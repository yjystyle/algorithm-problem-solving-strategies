cache = [[-1] * 101] * 101
W = '*p*'
S = 'help'
def matchMemoized(w: int, s: int) -> bool:
    ret = cache[w][s]
    if ret != -1:
        return ret
    while s < len(S) and w < len(W) and (W[w] == '?' or W[w] == S[s]):
        w = w + 1
        s = s + 1
    if w== len(W):
        ret = s== len(S)
        return ret
    if W[w] == '*':
        for skip in range(0, len(S) - s + 1):
            if matchMemoized(w+1, s+skip):
                ret = 1
                return ret
    return 0

ret = matchMemoized(0, 0)
print(cache)