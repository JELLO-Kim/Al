import sys

# 내가 푼 방법 => 코드 구현 시간이 오래 걸린다. (조건 없이 모두 중첩 반복문을 진행해야 하기 때문으로 보인다.)
N = int(input())
t=1 # 임시 변수 t에 1의 값을 선언한다. 이는 자연수 2가 무조건 소수이므로 소수의 갯수를 2를 포함하여 1개부터로 counting 하기 위함이다.
for row in range(3, N+1): # 반복문은 2를 제외하고 3부터 input값 까지 진행되도록 한다.
    for one in range(2, row): # 반복문을 진행하는 자연수 하나의 값이 소수인지 확인한다. 
        if row%one==0:
            break
    else:
        t+=1
print(t)


# 아리스토테세츠 체 사용
N = int(input())
t=[0]*(N+1) # 임시 변수 t를 input값인 N개 +1개만큼의 0 이 들어있는 list로 선언한다.
cnt=0 # 소수가 발견됐을때마다 1씩 증가하는 변수 cnt를 0으로 초기화 해준다.
for row in range(2, N+1): # 소수판정이 시작될 수인 2부터 N+1까지 반복문을 진행한다.
    if t[row]==0: # list로 선언된 변수 t의 row번째 자리가 0이라면 cnt의 값을 1 추가한다. 
        cnt+=1
        for j in range(row, N+1, row): # 해당 수의 배수들은 소수가 아니므로 값을 0에서 1로 바꿔준다.
            t[j]=1
print(cnt)


