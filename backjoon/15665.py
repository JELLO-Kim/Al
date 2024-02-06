import sys
import copy
from itertools import *
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
k = sorted(set(list(map(int, input().split()))))
def DFS(l, idx):
    if l == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, len(k)):
        ans.append(k[i])
        DFS(l+1, i)
        ans.pop()
ans = []
DFS(0, 0)