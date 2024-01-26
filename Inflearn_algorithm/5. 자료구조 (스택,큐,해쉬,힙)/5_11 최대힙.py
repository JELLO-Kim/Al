# 최대힙 (heapq)
# 자연수의 부호를 바꿔서 heapq 를 하면 최소힙 이 아닌 최대힙 형태로 완전이진트리를 구성한다.
"""
5
3
6
0
5
0
2
4
0
-1

출력
6
5
5
"""
import sys
import heapq as hq
sys.stdin = open("input.txt", "r")

a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) ==0:
            print((-1))
        else:
            print(-hq.heappop(a))  # a의 루트노드 값을 pop 시킬때, push 당시 음수로 변환한것을 원복해준다.
    else:
        hq.heappush(a, -n)  # a list에 n의 음수 값을 push 한다. (최대힙의 형태로 들어간다.)
