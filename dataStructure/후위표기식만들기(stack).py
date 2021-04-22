import sys
# 주어진 전위표기식을 후위표기식으로 표현하기
# stack 사용
n = input()
stack=[]
res=""
for i in n:
    if i.isdecimal(): # 숫자라면 계산식에 바로 추가
        res+=i
    else: # 연산자라면 규칙에 맞게 stack list에 추가하거나 계산식으로 배치한다
        if i=='+' or i=='-': # 반복문을 도는 것이 + 나 -일 경우 이전의 연산자들 (괄호 건드리지 않게) 을 모두 pop 해준다.
            while stack and (stack[-1] == "+" or stack[-1] =='-' or stack[-1] == "*" or stack[-1] == "/") and stack[-1] != "(":
                res+=stack.pop()
        if i=="*" or i =="/": # *s나 /일 경우 마지막 연산자가 *나 /가 아닐때까지 pop 해준다
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                res+=stack.pop()
        if i==")": # 닫는 괄호가 올 경우 여는 괄호 범위까지 pop 해준다. 여는 괄호도 stack에서 제거해준다
            while stack and stack[-1] != "(":
                res+=stack.pop()
            if stack[-1] == "(":
                stack.pop()
            continue
        stack.append(i)

for j in stack[::-1]: # stack에 남은 연산자들을 뒤에서부터 pop 해준다.
    if j == "+" or j == "-" or j == "*" or j =="/":
        res+=j

print(res)