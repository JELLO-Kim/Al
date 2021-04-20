import sys

# 좌측, 우측 끄트머리부터 숫자를 뽑아 최대길이의 증가수열 만들기

# 내가 푼 코드
sys.stdin=open("input.txt", "rt")
n = int(input())
l = list(map(int, input().split()))

lt=0
rt=n-1
res=[] # 증가수열이 담길 list
txt="" # 증가수열의 방향에대한 정보가 담길 빈 string

while lt<=rt: # 반복문 진행 조건
    if len(res)==0: # 첫번째 숫자일 경우 단순히 기존 list에서만 비교한다
        if l[lt]<l[rt]:
            res.append(l[lt])
            lt+=1
            txt+="L"
        else:
            res.append(l[rt])
            rt-=1
            txt+="R"
    else: # 하나이상의 값이 res에 있을 경우 res의 마지막 값과도 고려한다
        left=l[lt]
        right=l[rt]
        if res[-1] < left and res[-1] < right: # list의 값이 res의 마지막 값보다 둘다 클 경우 list의 값중 작은 값을 넣는다
            if l[lt]<l[rt]:
                res.append(l[lt])
                lt+=1
                txt+="L"
            else:
                res.append(l[rt])
                rt-=1
                txt+="R"
        elif res[-1] < left and res[-1] > right: # res와 비교하여 left가 더 크고 right는 오히려 작을 경우 right는 버리고 left를 사용한다
            res.append(left)
            txt+="L"
            lt+=1
        elif res[-1] > left and res[-1] < right: # 위의 반대 경우이다
            res.append(right)
            txt+="R"
            rt-=1
    if l[lt]<res[-1] and l[rt] < res[-1]: # res와 비교하여 list의 좌측과 우측값이 모두 작을 경우 반복문을 종료한다
        break
    if lt==rt: # 비교조건이 동일할 경우 반복문을 종료한다
        break
print(len(res), txt)

# 수아님 코드 (더욱 간결해졌다.)
# 증가수열 만들기(그리디)
n=int(input())
a=list(map(int, input().split()))
cnt=0
tmp=0
s=""
for i in range(n):
    if min(a[0], a[-1])==a[0] and a[0]>tmp or a[0]>tmp and a[-1]<=tmp:
        s+="L"
        tmp=a.pop(0)
        cnt+=1
    elif min(a[0], a[-1])==a[-1] and a[-1]>tmp or a[-1]>tmp and a[0]<=tmp:
        s+="R"
        tmp=a.pop()
        cnt+=1
print(cnt)
print(s)