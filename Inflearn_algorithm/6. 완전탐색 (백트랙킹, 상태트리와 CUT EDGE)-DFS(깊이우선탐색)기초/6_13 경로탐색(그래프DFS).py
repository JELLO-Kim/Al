import sys
import time
start = time.time()
sys.stdin=open("input.txt")
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(9)]

s = [[0]*(n+1) for _ in range(n+1)]

for i in a:
    s[i[0]][i[1]] = 1
"""
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0]
[0, 1, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 0, 1]
[0, 0, 0, 0, 0, 0]
"""
cnt = 0
ch = [0]*(n+1)
def DFS(L):
    global cnt
    if L == 5:
        for j in path:
            print(j, end=" ")
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if s[L][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                ch[i]= 0
                path.pop(-1)
ch[1] =1
path = [1]
DFS(1)
print(cnt)
end = time.time()

print(f"소요시간 : {end-start}")

# 0.00013208389282226562
# 0.00013017654418945312