# ord() 활용하여 숫자값 구하기
"""
WA -> 13
"""
aa = {chr(i): (i-65)//3+2 for i in range(ord("A"), ord("Z")+1)}
aa.update({
    "S": 7,
    "V": 8,
    "Y": 9,
    "Z": 9
})
answer = 0
for i in input():
    answer += aa[i]+1
print(answer)