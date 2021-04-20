import sys
# 주어진 횟수만큼 가장 큰값에서 1을 빼 가장 작은값에 더해준 뒤 최종적으로 가장 큰값과 가장 작은값의 차 구하기

n = int(input())
l = list(map(int, input().split()))
print(l)
m = int(input())

t=0
while t!=m:
    #최대값 찾기
    maxx=max(l)
    # 그 값의 인덱스 찾기
    idx_max = l.index(maxx)
    # 최솟값 찾기
    minn=min(l)
    # 그 값의 인덱스 찾기
    idx_min = l.index(minn)

    # 최대값에서 최소값으로 1 주기
    maxx-=1
    minn+=1
    # list 새로 갱신하기
    l[idx_max]=maxx
    l[idx_min]=minn

print(max(l)-min(l))

# 정렬 후 값 구하기
l.sort(reverse=True)
j=0
while j!=m:
    l[0]-=1
    l[-1]+=1
    l.sort(reverse=True) # 값 설정 후 list 재 정렬해주기 (항상 큰값이 처음, 작은 값이 나중으로 오도록)
    j+=1
print(l[0]-l[-1])

