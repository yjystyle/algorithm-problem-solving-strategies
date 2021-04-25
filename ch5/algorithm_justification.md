# 5. 알고리즘 정당성 증명
## 5.1 도입
- 대부분의 프로그래머들은 알고리즘을 쓰고 싶어하지 증명하고 싶어하지 않는다.
- 그럼에도 불구하고 의사코드에 대한 증명을 이해해야 공부가 된다.
- 직관도 생긴다.
- 이 책에는 모든 정당성에 대한 증명을 담고 있으니 좋은 책

<br>

## 5.2 수학적 귀납법과 반복문 불변식
### 100개의 도미노
```
- 첫번째 도미노는 직접 손으로 밀어서 쓰러뜨린다.
- 한 도미노가 쓰러지면 다음 도미노도 역시 반드시 쓰러진다.
```
- 도미노처럼 수학적 귀납법은 반복적인 구조를 갖는 명제들을 증명한다.
- 순서
    - 단계 나누기
    - 첫 단계 증명
    - 귀납 증명
- 사다리 예제를 통한 귀납법 증명

<br>

### 반복분 불변식
- 귀납법을 통해 알고리즘의 정당성을 증명할 때는 반복문 불변식이라는 개념 도입
    - 반복문 불변식 : 반복분의 내용이 한 번 실행될 때마다 중간 결과가 우리가 원하는 답으로 가는 길 위에 잘 있는지를 명시하는 조건
- 순서
    - 반복문 진입시 불변식의 성립함 보이기
    - 반복문 내용이 불변식을 깨뜨리지 않음을 보이기
    - 반복문 종료시 불변식의 성립 여부 보이기

<br>

### 이진 탐색과 불변식
```python
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
```
<br>

### 삽입 정렬과 반복문 불변식
```python
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

ret = insertion_sort([12, 11, 13, 5, 6])
print(ret)
```
<br>

## 5.2 귀류법
- 우리가 원하는 바와 반대되는 상황을 가정하고 논리를 전개해서 결론이 잘못됐음을 찾아내는 증명 기법
