import sys
sys.stdin=open("input.txt", "r")
# 입력 속도 빠르게 하기
# input=sys.stdin.readline
# 문자열 입력시
# s=input().rstrip()

# DFS 방법 사용하지 않고 중첩 반복문으로 풀었을 경우
if __name__=='__main__':
    a, m = map(int, input().split())
    n=list(range(1, a+1))
    res=[]
    for i in range(a):
        for j in range(a):
            cnt=[n[i], n[j]]
            res.append(cnt)

    for i in res:
        print(str(i[0]), str(i[1]))
        
    print(len(res))


# DFS 방법
def DFS(x):
    global cnt
    if x==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[x]=i
            DFS(x+1)

if __name__=='__main__':
    n, m = map(int, input().split())
    res=[0]*m
    cnt=0
    DFS(0)
    print(cnt)
