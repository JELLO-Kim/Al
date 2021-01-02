# N부터 1까지 한줄에 하나식 출력하기

N=int(input())
for i in range(1, N+1):
    print(str(N))
    N -= 1

# 다른 사람의 풀이 (더 짧긴 하다. 이게 더 좋은가?)
print("\n".join(map(str,range(int(input()),0,-1))))