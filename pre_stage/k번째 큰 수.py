import sys
N, K = map(int, input().split())
card = list(map(int, input().split()))
pre=set() #set 형태의 pre 변수를 선언한다.
for one in range(N): # 첫번째 카드
    for two in range(one+1, N): # 두번째 카드
        for three in range(two+1, N): # 세번째 카드
            pre.add(card[one]+card[two]+card[three]) # set은 append가 없어 add로 더해준다. / 각 카드의 합을 pre에 저장한다.
pre=list(pre) # set 형태의 pre를 list로 변환해준다
pre.sort(reverse=True) # 내림차순으로 정렬한다.
print(pre[K-1]) # 0부터 시작하는 index이기 때문에 k-1번째 수를 출력한다.