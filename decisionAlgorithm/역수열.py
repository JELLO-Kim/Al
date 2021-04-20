import sys

# 혼자 해결 못한 문제
# 기존의 값을 하나씩 제거하여 조건에 맞춘 뒤 값 결정하기
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0): # 자기보다 큰 숫자갯수가 0개가 되었고, 현재위치에 0이 있을 경우 값이 결정된다
            seq[j]=i+1
            break
        elif seq[j]==0: # 아직 자기보다 큰 숫자가 남아있는데 seq의 자리에는 0이라면 a[i]의 수를 하나씩 줄인다
            a[i]-=1

for x in seq:
    print(x, end=' ')