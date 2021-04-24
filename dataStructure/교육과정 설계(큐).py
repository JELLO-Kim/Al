import sys
from collections import deque

goal = list(input()) # 맞춰야 하는 수업 커리큘럼
n = int(input())
s = []
for _ in range(n):
    s.append(list(input()))
t=1
for j in s:
    g = deque(goal) # 수업 커리큘럼을 deque 파라미터로 넣어 그 값을 g 로 관리한다
    j = deque(j) # 반복문을 돌고있는 j 역시 deque 파라미터로 넣어 그 값을 새로 j 라고 명명한다.
    for i in j:
        if i in g: # 커리큘럼에 해당하는 과정일 경우
            cr = g.popleft() # 변수에 커리큘럼의 최 좌측 하나를 빼어 변수에 담는다
            if cr!=i: # 변수에 담은 값과 반복문의 값이 같지 않을 경우, 즉 커리큘럼 순서대로 배정하지 않았을 경우
                print(f"#{t} NO")
                break
        if not g: # 커리큘럼을 모두 올바르게 소진했을 경우
            print(f"#{t} YES")
            break
    t+=1