import sys
from collections import deque
# 내가 푼 코드
n, k=map(int, input().split())
prince=list(range(1, n+1))
prince=deque(prince)
t=1 # k번째 까지 반복해주기 위해 변수 t를 선언한다. 첫번째부터 바로 진행되므로 1값을 준다
while len(prince)!=1: # 한명의 왕자가 남을때까지 반복되도록 한다.
    cr = prince.popleft() 
    prince.append(cr)
    t+=1 # 한번 수행 후 t값을 1씩 올린다
    if t==k: # t값이 조건 k값과 같다면 해당 왕자는 오른쪽으로 이동하지 않고 제외된다.
        prince.popleft()
        t=1
print(prince[0])
