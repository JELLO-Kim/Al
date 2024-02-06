import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
num = [str(a) for a in range(1, n+1)]

ch = []

def DFS(l):
    if l == m:
        print(" ".join(ch))
    else:
        for row in num:
            ch.append(row)
            DFS(l+1)
            ch.pop()

DFS(0)