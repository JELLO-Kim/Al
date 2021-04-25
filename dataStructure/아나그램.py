import sys
sys.stdin=open("input.txt", "r")
n=list(map(str, input())) # 비교대상이 되는 문자열은 list에 담아 remove 가능한 형태로 만든다
m=input() # 비교주체는 그대로 string 형태로 둔다. (반복문으로 한 문자씩 가능하니까)

for i in m: # m의 문자 하나씩 반복문을 돌려 확인한다
    if i in n: # 해당 문자가 n list에 있을 경우 n list에서 그 문자열을 제외해준다 (기본적으로 소문자와 대문자가 구분된다)
        n.remove(i)
if not n:
    print("YES") # 최종결과 아나그램이므로 n list가 비게 되면 YES
else:
    print("NO") # 그렇지 않을 경우 NO