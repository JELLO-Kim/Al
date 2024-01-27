# 이전까지는 이진트리였지만 이번 문제는 중복을허용한다

import sys
sys.stdin = open("input.txt", "r")

def DFS(now=""):
    global res
    if len(now) == M:
        print(now[0] + " " + now[1])
        res += 1
        return
    for i in range(1, N+1):
        DFS(now+str(i))



if __name__ == "__main__":
    N, M = map(int, input().split())
    res = 0
    DFS()
    print(res)
    