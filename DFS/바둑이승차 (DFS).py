import sys
sys.stdin=open("input.txt", "r")

def DFS(d, k, tsum):
    global result
    # 젤 마지막요소 함수진행 전에 미리 확인하기. 전체무게-현제 레벨까지 총무게+남은 한마리의 무게 < 현재기준 조건충족 최고무게 일 경우 굳이 함수진행하지 않는다.
    if k+(total-tsum)<result:
        return
    # 무게 제한 확인
    if k>n: 
        return
    # 마지막 index일 경우 처리해주기
    if d == m: 
        if k>result:
            result=k
    else:
        DFS(d+1, k+a[d], tsum+a[d])
        DFS(d+1, k, tsum+a[d])


if __name__=='__main__':
    n, m = map(int, input().split()) # n=259, m=5
    a=[int(input()) for _ in range(m)] # a = [81, 58, 42, 33, 61]
    result=-1234
    total=sum(a)
    DFS(0, 0, 0)    