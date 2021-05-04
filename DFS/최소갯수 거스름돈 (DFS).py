import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global cnt
    res=0
    # 컷조건1 : 거스름돈금액보다 합이 클 경우 or 이미 구한 최소갯수보다 횟수가 많아질 경우
    if sum>m or L>cnt:
        return
    # 결과저장 : 거스름돈만큼 합이 나왔을때 => 그 횟수가 현재기준 최소라면 결과로 최솟값 저장.
    if sum==m:
        if L<cnt:
            cnt=L
    for i in range(n):
        DFS(L+1, sum+k[i])

if __name__=='__main__':
    n = int(input())
    k = list(map(int, input().split()))
    m = int(input())
    # 큰 수부터 우선 적용 시키기 => 속도 향상!!!
    k.sort(reverse=True)
    cnt=214000000
    DFS(0, 0)
    print(cnt)