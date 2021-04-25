import sys
sys.stdin=open("input.txt", "r")
'''
딕셔너리 활용 첫번째 버전 : 두개의 딕셔너리 형태를 활용
'''
n=input()
m=input()

str1=dict()
str2=dict()

for i in n: # 해당 문자열의 갯수를 각각 카운팅 해주기
    str1[i]=str1.get(i, 0)+1

for i in m:
    str2[i]=str2.get(i, 0)+1

for i in str1.keys(): # str1 dict의 key값만 가져오기
    if i in str2.keys(): # str1의 key 하나하나가 str2 의 key에 존재한다는 조건
        if str1[i]!=str2[i]: # 문자열은 존재하지만 그 갯수가 다르다면 아나그램이 아니다
            print("NO")
            break
    else: # 일치하는 문자열이 없을 경우 아나그램이 아니다
        print("NO")
        break
else: # 정상적으로 반복문이 종료되었을 경우 for의 else문이 실행된다
    print("YES")

'''
기존의 딕셔너리 활용 방법을 개선한 버전이다 : 한개의 딕셔너리를 활용
'''

n=input()
m=input()

sH=dict()
str2=dict()

for i in n: # n 문자열의 각각 문자에 해당하는 값을 1씩 더해주기
    sH[i]=sH.get(i, 0)+1
for i in m:
    sH[i]=sH.get(x, 0)-1 # m 문자열의 각각 문자에 해당하는 값을 1씩 빼주기

for x in n:
    if sH.get(x)>0: # 다시 감소되었는데도 값이 0이 아닐경우 아나그램이 아니다
        print("NO")
        break
else:
    print("YES")