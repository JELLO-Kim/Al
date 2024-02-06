import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()


def DFS(l, ch):
    if l == m:
        for i in ch:
            print(i, end=" ")
        print("")
    else:
        for j in num:
            if j not in ch:
                ch.append(j)
                DFS(l+1, ch)
                ch.pop()

ch = []
for row in num:
    ch.append(row)
    DFS(1, ch)
    ch.pop()
