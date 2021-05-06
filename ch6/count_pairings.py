# 총 학생수
n = 3
are_friends = [[False for i in range(10)] for j in range(10)] 
taken = [False for i in range(10)]


def count_pairings(taken):

    # 남은 학생들 중 가장 번호가 빠른 학생 찾기
    first_free = -1
    for i in range(n):
        if not taken[i]:
            first_free = i
            print(first_free)
            break
    
    # 기저사례 : 모든 학생이 짝을 찾았으면 한가지 방법을 찾았으니 종료하기
    # 위의 if문을 안탄 경우, taken이 모두 True 인 경우
    if first_free == -1:
        return 1
    
    ret = 0
    for pair_with in range(first_free +1, n):
        if not taken[pair_with] and are_friends[first_free][pair_with]:
            taken[first_free] = taken[pair_with] = True
            ret = ret + count_parings(taken)
            taken[first_free] = taken[pair_with] = false

    
count_pairings(taken)
