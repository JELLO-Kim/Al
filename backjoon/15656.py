import sys
sys.stdin = open("input.txt", "r")

# from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

def DFS(l, ch):
    if l == m:
        print(*ch)
    else:
        for j in num:
            ch.append(j)
            DFS(l+1, ch)
            ch.pop()

ch = []
for row in num:
    ch.append(row)
    DFS(1, ch)
    ch.pop()