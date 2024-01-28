# 상태트리 nCm 구하기
import sys
import time
sys.stdin = open("input.txt", "r")


def DFS(L, s):
    global cnt
    if L == m:
        for row in res:
            print(row, end=" ")
        cnt += 1
        print()
        return
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1, i+1)



if __name__ == "__main__":
    start = time.time()
    n,m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0, 1)
    print(cnt)