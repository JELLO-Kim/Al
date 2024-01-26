# 쇠막대기
import sys
sys.stdin = open("input.txt")

def sol():
    stack = []
    laser = sys.stdin.read()
    sum = 0
    for x in laser:
        if x == "(":
            stack.append(x)
        else:
            stack.pop()
            if stack:
                if stack[-1] == "(":
                    sum += len(stack)
                else:
                    sum += 1
    print(sum)
sol()