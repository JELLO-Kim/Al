# X 보다 작은 수
import sys
input = sys.stdin.readline
def my_sol():
    # input()
    # X = int(input())
    # A = list(map(int, input().split()))
    N, X = 10, 5
    A = [1, 1,0 ,4 ,9 ,2 ,3 ,8 ,5 ,7 ,6]
    res = "".join([str(i) for i in A if i<X])
    print(res)

def short_sol():
    n,x,*a=map(int,open(0).read().split())
    for i in a:i<x!=print(i)

"""
open 메소드 확인하기!
"""