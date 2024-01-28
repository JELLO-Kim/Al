# 상태트리 nCm 구하기
import sys
import time
sys.stdin = open("input.txt", "r")
"""
5 3
2 4 5 8 12
6

출력 : 2
"""
def DFS(L, s, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = num_list[i]
            DFS(L+1, i+1, sum+num_list[i])
            



if __name__ == "__main__":
    start = time.time()
    n,k = map(int, input().split())
    num_list = list(map(int, input().split()))
    m = int(input())
    res = [0]*k
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)