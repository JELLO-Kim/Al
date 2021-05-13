# Greedy
<br>

# 문제 예제

## 1. 큰 수의 법칙

>n만큼 길이로 주어진 배열들중 중복을 허용해서 k번을 더하여 가장 큰수를 구하자 단, 같은 수는 m번까지만 연속으로 사용할 수 있다! index가 다른 같은 수일 경우 다른 존재로 인식한다.


#### input.txt 내용
```
5 8 3
2 4 5 4 6
data 불러오기
n, k, m = map(int, input().split())
data = list(map(int, input().split()))
```

#### Sol1 : 일반적인 풀이
```python
n = 5
k = 8
m = 3
data = [2, 4, 5, 4, 6]

# data를 내림차순으로 정렬
data.sort(reverse=True)

# 가장 큰 수
first = data[0]
# 두번째로 큰 수
second = data[1]

# 가장큰 수를 m번만큼 연속되게 더한 후 두번째로 큰수를 한번 더하는 조합으로 k번째까지 합산한다.
result=0
while True:
    # 더해야 하는 총 횟수 k 번을 충족했을 시 break
    if k==0:
        break
    for i in range(m):
        # for문 진행중에 더해야 하는 총 횟수 k 번을 충족했을 시 break
        if k==0:
            break
        result+=first
        # 한번 합할때마다 k의 횟수 차감
        k-=1
    # 가장큰 수를 m번연속하여 더한 후 두번째로 큰 수 더하기
    result+=second
    k-=1
print("answer 1 :", result)
```
- 정답 : 46
- 출력 : 46

> 만약 가장 큰수가 아닌 가장 작은수를 구하고자 한다면 sort()로 오름차순 정렬로만 바꿔주면 된다.

#### Sol2 : 반복되는 수열 파악하기
```python
'''
n = 5
k = 8
m = 3
data = [2, 4, 5, 4, 6]
data.sort(reverse=True)
first = data[0]
second = data[1]

반복되는 수열 = 가장 큰수*k번 + 두번째로 큰 수
위의 예시로는 [ 6 6 6 5 ]
'''
k=8
# 반복되는 수열의 총 횟수 : 8//(3+1)=2
count = k//(m+1)
# 반복되는 수열 속 가장 큰 수가 더해지는 횟수 : 2*3 = 6
count = (k//(m+1))*m
# 만약 나누어서 나머지가 있는 경우에는 큰 수만 그만큼 더 더하면 된다
count += k%(m+1)

result = 0
result = count*first
result += (k-count)*second

print("answer 2 :", result)
```
<br>
<br>

## 2. 1이 될때까지 수 정리하기

> 숫자 n과 k가 주어진다. n이 k로 나누어 떨어지면 k로 나누고, 그렇지 않을 경우 n에서 1씩 빼서 최종적으로 숫자 1을 만들자고 할때 수행해야 하는 최소 횟수를 구하여라

#### input.txt 내용
```
25 5
```

#### Sol1 : 일반적 풀이
```python
n, k = map(int, input().split())
cnt = 0
while n!=1:
    if n%k == 0:
        n = n//k
        cnt+=1
    else:
        n -= 1
        cnt+=1
print(cnt)
```