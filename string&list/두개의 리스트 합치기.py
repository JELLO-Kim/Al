# import sys
# # 내가 푼 코드 1
N=input()
N_list=list(map(int, input().split()))
M=input()
M_list=list(map(int, input().split()))

tot=N_list+M_list
tot.sort()

for i in tot:
    print(i, end=' ')

# sort() 사용하면 nlonN 번 실행하게 됨
# N_list와 M_list를 먼저 오름차순으로 정렬하고 합치는 방식 선택하기

# 내가 푼 코드 2
import sys
N=input()
N_list=list(map(int, input().split()))
M=input()
M_list=list(map(int, input().split()))

N_list.sort()
M_list.sort()
tot=[]
for i in range(int(N)+int(M)):
    if not N_list:
        tot = tot+M_list
        break
    if not M_list:
        tot = tot+N_list
        break
    if N_list[0]<=M_list[0]:
        tot.append(N_list[0])
        del N_list[0]
    else:
        tot.append(M_list[0])
        del M_list[0]
for t in tot:
    print(t, end=' ')


# 소스코드
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')