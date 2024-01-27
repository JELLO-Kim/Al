import sys
import time
sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L == M:
        for j in range(L):
            print(res[j], end= " ")
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            if ch[i]== 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0     

if __name__ == "__main__":
    start = time.time()
    N, M = map(int, input().split())
    res = [0]*N
    ch = [0]*(N+1)
    cnt = 0
    DFS(0)

    end = time.time()
    print(f"time : {end-start}")