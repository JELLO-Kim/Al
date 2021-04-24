import sys
from collections import deque
sys.stdin=open("input.txt", "rt")

# 내가 푼 방법 : 딕셔너리 없이 for문 검사를 통해 계산하였다.
n = int(input())
k = [input() for _ in range(n)]
t = [input() for _ in range(n-1)]

for i in k:
    if i not in t:
        print(i)
        break

# 소스코드 : "해쉬" 방법 사용

n = int(input())
p=dict() # 딕셔너리 형태 변수를 하나 선언해준다
for i in range(n):
    word=input() # 노트에 적은 단어를 Key로 하여 그 값에 1을 넣어준다
    p[word]=1
for i in range(n-1): # 시에 진짜 쓰인 단어의 값을 0으로 바꿔준다
    word=input()
    p[word]=0

for key, val in p.items(): # 최종적으로 모든 형태의 딕셔너리의 key와 val값을 검사한다.
    if val==1: # 노트엔 적혔지만 시에는 사용되지 않아 값이 여전히 1인것이 발견될 경우 출력한다.
        print(key)
        break