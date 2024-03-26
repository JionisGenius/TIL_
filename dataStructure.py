# 이게 "진짜" 다
# data sttructure

# queue 구현할때 deque로 구현해야하므로 collections 라이브러리사용

from collections import deque

# 리스트에서 맨 앞쪽에 있는 원소 (삽입/삭제)의 시간복잡도는 O(N)
# append()/ pop() 매서드는 맨 뒤 원소 기준으로 삭제하기때문 맨 마지막 원소(삽입/삭제)의 시간복잡도는 O(1)
# deque 시간복잡도 O(1)

# deque 사용법
# 첫번째원소 제거 할때 popleft()
# 마지막원소 제거 할때 pop()
# 첫번째원소x 삽입 할때 appendleft(x)   
# 마지막원소x 삽입 할때 append(x)

# 따라서 queue 구현시 
# append() / popleft() 사용 

data = deque([1,2,3,4])

data.appendleft(0)
data.append(5)

print(data)
print(list(data)) # list transformat

# Collections Counter : 원소 등장 횟수 세기 기능
from collections import Counter
C = Counter(['a',"bee",'c'])
print(Counter('a'))
print(dict(C)) # 자료형 변환


queue = deque() # queue 구현 , deque 라이브러리 사용
queue.extend([1,2,3]) # 개쩔탱 extend 
queue.appendleft(0)
queue.pop()
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# ㅎㅎ ㄳㄳ
# 재귀함수 recursive_function #DFS#BFS

def re_func(i): 
    if i==10:
        return
    print( i, "번째 함수에서", i+1, "번째 함수 호출")
    re_func(i+1)
    print( i, "번째 함수 종료")
    
re_func(0)

# 터미널 지우기
# import os
# os.system('cls')

# 재귀함수 vs 반복문 : 결론 재귀함수가 코드가 더 간결하다!
#  pactorial

# 반복문으로 구현한 n!
def iterator(n):
    result =1 # 1*n 
    for i in range(1,n+1): # 1부터 n까지 동작
        result *= i

 # 재귀함수로 구현한 n! 
def recursive(n):
    if(n<=1):
        print(1)
        return 1
    result = (n*recursive(n-1))
    # print(result)
    return result

recursive(8)
 
