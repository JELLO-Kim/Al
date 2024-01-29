import sys
from time import time
sys.stdin = open("input.txt", "r")
start = time()
k = int(input())  # 3
weight = list(map(int, input().split())) # [1,5,7]
# weight.sort()
s = sum(weight)
res = set()
def DFS(L, sum):  # L = 추 index, sum = 추의 합
    if L == k:  # 추 3개 모두 확인함
        if 0 < sum <= s:
            res.add(sum)
        return
    # 1. 무게에 사용하는 버전
    DFS(L+1, sum+weight[L])
    # 2. 그릇에 사용하는 버전
    DFS(L+1, sum-weight[L])
    # 3. 아예 사용하지 않는 버전
    DFS(L+1, sum)


for target in range(k):
    DFS(target, 0)  # 1~13까지 target의 무게 확인하기
print(s - len(res))
end = time()

print(f"소요시간 : {end-start}")