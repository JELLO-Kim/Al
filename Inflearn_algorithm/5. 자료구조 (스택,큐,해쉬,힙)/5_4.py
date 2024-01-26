# 후위식 연산 하기
"""
352+*9-
출력 : 12
"""
import sys
sys.stdin = open("input.txt")

def my_sol():
    stack = []
    q_list = input()

    for row in q_list:
        if row.isdecimal():
            stack.append(row)
        else:
            tmp_set = []
            for _ in range(2):
                tmp_set.append(stack.pop())
            if len(tmp_set) != 2:
                print("error !!")
                break
            stack.append(str(eval(tmp_set[1]+row+tmp_set[0])))
    print(stack[0])