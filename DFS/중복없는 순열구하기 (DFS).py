import sys
sys.stdin=open("input.txt", "r")
# sys.setrecursionlimit(1000)
# 입력 속도 빠르게 하기
# input=sys.stdin.readline
# 문자열 입력시
# s=input().rstrip()

def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0


if __name__=='__main__':
    n, m = map(int, input().split())
    res=[0]*(m+1)
    ch=[0]*(n+1)
    cnt=0
    DFS(0)