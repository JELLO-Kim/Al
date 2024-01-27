# 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성
"""
입력 : 11
출력 : 1011
"""
def DFS(x):
    if x//2 == 0:
        print(x%2,end="")
        return
    DFS(x//2)
    print(x%2,end="")

DFS(int(input()))