# 가장 큰 수 (스택)
"""
5276823 3
"""
"""
스택 : Last In First Out (LIFO)
"""
import sys
sys.stdin = open("input.txt")

def sol():
    stack = []
    num, m = sys.stdin.read().split()
    num = list(map(int, num))
    m = int(m)
    for x in num:
        while stack and m>0 and stack[-1] < x:
            stack.pop()
            m -= 1
        stack.append(x)
    if m >0:
        stack = stack[:-m]
    for i in stack:
        print(i, end="")
sol()