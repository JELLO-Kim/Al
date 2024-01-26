# 후위표기식 연산
"""
입1 : 3+5*2/(7-2)
출1 : 352*72-/+

입2 : 3*(5+2)-9
출2 : 352+*9-
"""
import sys
sys.stdin = open("input.txt")

def sol():
    stack = []
    res = ""
    q_list = input()
    for row in q_list:
        if row.isdecimal():
            res += row
        else:
            # (
            if row == "(":
                stack.append(row)
            elif row in ["*", "/"]:
                while stack and (stack[-1] in ["*", "/"]):
                    res += stack.pop()
                stack.append(row)
            elif row in ["+", "-"]:
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.append(row)
            elif row == ")":
                while stack and stack[-1] != "(":
                    res += stack.pop()
                stack.pop() # 여는 괄호 빼기
    while stack:
        res += stack.pop()



sol()