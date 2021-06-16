a=[1,5,2,4,7]

n = len(a)
cache = [-1 for col in range(100)]
ret = 0
#a[start]에서 시작하는 증가 부분 수열 중 최대 길이를 반환한다.
def lis2(start):
    #캐시에 값이 있으면 해당 값 리턴.
    ret = cache[start]
    if(ret != -1):
        return ret
    #항상 a[start]는 있기 때문에 길이는 최하 1.
    ret = 1
    #캐시에 값이 없는 경우
    for next in range(start+1, n):
        if a[start] < a[next]:
            #캐시에 최대 값을 넣는다.
            cache[start] = max(ret, lis2(next) + 1)
            ret = cache[start]
    return ret

maxLen = 0
for begin in range(0, n):
    maxLen = max(maxLen, lis2(begin))
    print(lis2(begin))

print(maxLen)