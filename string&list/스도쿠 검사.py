import sys
# 혼자의 힘으로 풀지 못했다. 소스코드이다.
def check(a):
    # 행과 열의 조건을 확인하는 반복문 검사하는 값에 대해서 생성한 리스트의 같은 숫자를 index로 갖는 부위를 1로 변환한다.
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9: # 생성한 리스트이 합이 9가 아닐 경우 스도쿠 조건을 충족하지 않음을 반환한다
            return False
    for i in range(3): # 9개의 스도쿠들 중 하나의 스도쿠를 골라내기 위한 반복문
        for j in range(3):
            ch3=[0]*10
            for k in range(3): # 이동되는 조건에 대한 변수 k
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a): # 스도쿠 조건을 충족할 경우 (True)
    print("YES")
else: # 스도쿠 조건을 충족하지 않을 경우 (False)
    print("NO")