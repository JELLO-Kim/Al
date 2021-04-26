import sys
import heapq as hq
'''
파이썬에서 heap을 사용하기 위해 "heapq"를 import 한다.
heappop = 가장 최상위의 것 (즉, 가장 작은 수)를 가져온다
heappush = 완전이진트리형식으로 heap구조에 의해 수를 push한다. (즉, 집어넣은 값의 상위 node에 더 작은 수가 있다면 상위 node의 값과 자리를 바꾸는걸 반복해 최종적으로 root node로부터 오름차순으로 자식 node가 형성된다)
'''
sys.stdin=open("input.txt", "r")

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)