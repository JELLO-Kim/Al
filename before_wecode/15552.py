# python 입출력 개선
import sys
sys.stdin=open("input.txt", "r")
input = sys.stdin.readline
T = int(input().rstrip())
for i in range(T):
    a, b = map(int, input().split())
    print(a+b)

# open 을 사용하면 더 빠르게 read 할 수 있다