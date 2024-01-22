import sys
input = sys.stdin.readline
N, M = map(int, input().split())
bucket_list=[0]*N
for row in range(M):
    i, j, k = map(int, input().split())
    for rrow in range(i-1, j):
        bucket_list[rrow] = k

print(*bucket_list)