import sys
# 내가 푼 코드
N = int(input())
K = [(input().split()) for _ in range(N)]

for idx, i in enumerate(K): #enumerate를 활용해 index와 값을 모두 얻는다.
    if i[0].lower()==i[0][::-1].lower(): # list의 역순배치를 활용해 두 값을 비교한다. 대소문자 구분이 없기 때문에 모두 소문자로 변환하여 비교한다.
        print(f"#{idx+1}", "YES") # 두개가 같다면 f-string을 사용해 index+1의 값과 함께 "YES" 출력
    else:
        print(f"#{idx+1}", "NO") # 두개가 다르다면 f-string을 사용해 index+1의 값과 함께 "NO" 출력