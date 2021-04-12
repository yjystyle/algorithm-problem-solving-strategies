# 실수배열 A, 각 위치에서의 M개 만큼의 이동 평균
def moving_average1(A, M):
  ret = []
  for i in range(M-1, len(A)):
    partial_sum = 0
    for j in range(0, M):
      partial_sum = partial_sum + A[i-j]
    ret.append(partial_sum/ M)
  return ret


result = moving_average1([1,2,3,4,5], 3)
print(result)