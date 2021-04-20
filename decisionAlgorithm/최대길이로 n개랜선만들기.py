import sys
# 이분법을 활용하는 문제
k, n = map(int, input().split())
m=[int(input()) for _ in range(int(k))]

def Count(len): # 주어진 값으로 list속 모든 랜선들을 잘라 몇개의 랜선이 생성되는지 확인하는 함수
    cnt=0
    for x in m:
        cnt+=(x//len)
    return cnt

lt=0
rt=max(m)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n: # n개 이상으로 자를수 있을 경우(허용)
        res=mid # 자른 조건의 랜선 길이를 담는다
        lt=mid+1 # 더 긴 범위로 이동시킨다
    else:
        rt=mid-1 # 더 짧은 범위로 이동시킨다
print(res)