# git push 잔디 테스트용 수정문구

T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print('Case #'+str(i+1)+':', str(A), '+', str(B), '=', A+B)