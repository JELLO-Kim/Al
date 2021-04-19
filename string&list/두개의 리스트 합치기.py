import sys
# 내가 푼 코드 1
N=input()
N_list=list(map(int, input().split()))
M=input()
M_list=list(map(int, input().split()))

tot=N_list+M_list
tot.sort()

for i in tot:
    print(i, end=' ')

# 모든 정보를 가져온뒤 sort를 진행해 N의 수가 많은 조건에서 진행된다.
# sort() 사용하면 nlonN 번 실행하게 되므로 비 효율적이라 판단하여 아래 코드로 리팩토링 해주었다.
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
    if not N_list: # 더이상 N_list에 값이 없을 경우
        tot = tot+M_list
        break
    if not M_list: # 더이상 M_list에 값이 없을 경우
        tot = tot+N_list
        break
    if N_list[0]<=M_list[0]: # N_list의 값이 M_list보다 작거나 같을 경우 N_list의 값을 tot에 append
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
p1=p2=0 # 초기값이 0인 두개의 변수를 선언한다.
c=[] # 비어있는 list를 선언한다.
while p1<n and p2<m: # 반복문 진행 조건 (두개의 list가 모두 소진될때까지 이다)
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