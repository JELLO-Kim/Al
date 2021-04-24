import sys
from collections import deque
# 내가 푼 코드 : 몇번째 환자인지 특정짓는 법을 몰라 실패
# 소스 코드
n, k=map(int, input().split())
p = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
p=deque(p)
cnt=0
while True:
    cur=p.popleft()
    if any(cur[1]<x[1] for x in p):
        p.append(cur)
    else:
        cnt+=1
        if cur[0]==k:
            break
print(cnt)