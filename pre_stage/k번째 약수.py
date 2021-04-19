import sys
n, k = map(int, input().split())
cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
    if cnt==k: # 해당 약수가 k 번째라면 반복문을 종료한다.
        print(i)
        break
else:
    print(-1)