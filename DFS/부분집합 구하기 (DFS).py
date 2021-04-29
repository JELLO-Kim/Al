import sys
sys.stdin=open("input.txt", "r")

# 상태트리

def DFS(x):
    if x==n+1:
        for i in range(1, n+1):
            if ch[i]==1: # 값이 1인것 즉, 부분집합으로 뽑아내고자 처리했던 값들을 출력한다.
                print(i, end=' ')
        print() # 부분집합 별로 줄바꿈 처리
    else:
        ch[x]=1 # 해당 x 값을 부분집합으로 지정하는 값에 대해 1로 변경
        DFS(x+1) # 이후 x+1 단계 진행
        ch[x]=0 # 해당 x 값을 부분집합으로 포함하지 않도록 0으로 지정
        DFS(x+1) # 이후 x+1 단계 진행


if __name__=='__main__':
    n=int(input())
    ch=[0]*(n+1) # n개까지만 필요하지만 여유분으로 n+1개 길이만큼 생성
    DFS(1)