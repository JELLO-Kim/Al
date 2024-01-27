import sys
import time
sys.stdin = open("input.txt", "r")


def DFS(L, sum):
    global res
    # 아래 cut 차이로 원래 1.8 초 걸리던게 0.006초로 단축됨
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(N):
            DFS(L+1, sum+coin_list[i])
    
if __name__ == "__main__":
    start = time.time()
    N = int(input())
    coin_list = list(map(int, input().split()))
    coin_list.sort(reverse=True)
    m = int(input())
    res = 21740000000
    DFS(0,0)
    print(res)
    end = time.time()
    print(f"time : {end-start}")