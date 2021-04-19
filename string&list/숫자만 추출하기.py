import sys
# 내가 푼 코드
N = input()
K = len(N)
num=""
for i in range(K):
    try:
        if type(int(N[i])) is int:
            num+=N[i]
    except:
        pass
res=int(num)
cnt=0
for j in range(1, res+1):
    if res%j==0:
        cnt+=1

print(res)
print(cnt)

# 소스코드
N=input()
res=0
for i in N:
    if i.isdecimal():
        res=res*10+int(i)
print(res)
cnt=0
for i in range(1, res+1):
    if res%i==0:
        cnt+=1
print(cnt)