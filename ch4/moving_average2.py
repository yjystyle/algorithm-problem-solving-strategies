# 이동평균 구할때 중복되는 부분없이
# 뒤에꺼 빼고 앞에꺼 넣는 식으로
def moving_average2(A, M):
  partial_sum = 0
  ret = []
  # 앞에꺼 부분합 구하기
  for i in range(0, M-1):
    partial_sum = partial_sum + A[i]
  
  for i in range(M-1, len(A)):
    partial_sum = partial_sum + A[i]
    ret.append(partial_sum / M)
    
    # 가장 앞의 원소를 하나 제거한 값을 (-) 한다.
    partial_sum = partial_sum - A[i-M+1]
  return ret
  
result = moving_average2([1,2,3,4,5], 3)
print(result)