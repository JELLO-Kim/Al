import sys
sys.stdin=open("input.txt", "r")

def DFS(L, sum): # L = level을 의미한다.
    if sum>total//2: # 속도 향상을 위한 조건문이다 / 부분집합이 이미 전체합의 절반을 넘겼을 경우 더이상 검사할 필요가 없다
        return
    if L==n:
        if sum==(total-sum): # 조건에 맞는 부분집합이 있을 경우 여기에 해당된다.
            print("YES")
            sys.exit(0) # 프로그램 전체를 종료시킨다. 때문에 아래 조건문에서 NO가 출력되지 않는다.
    else:
        DFS(L+1, sum+a[L]) # 현재 값을 부분집합으로 포합하는 조건
        DFS(L+1, sum) # 현재 값을 부분집합으로 포함하지 않는 조건

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    total=sum(a)
    DFS(0,0) # 초기값으로 0번째에 합이 0인 값을 parameter로 넘긴다.
    print("NO") # 프로그램이 종료되지 않았을 경우, 즉 조건에 맞는 부분집합이 없을 경우 이 문자열이 출력된다.