# 1912 - Python
![](https://images.velog.io/images/c_hyun403/post/f47a1be3-0efc-4c51-86a9-1e06df84257b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.41.51.png)![](https://images.velog.io/images/c_hyun403/post/8401808d-5601-41dc-b32b-8c7ce8eca54e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.42.02.png)
숫자들의 연속된 합 중 가장 큰 값을 골라내는 문제이다.
가장 왼쪽서부터 값을 더해나가면서 (i-1까지의 합+i값까지의 합) 이 오리지널 i 의 갑보다
1. 크다면 : i 까지 포함하여 연속되게 합을 구하는 것이 최댓값에 가까워지는 것이다.
2. 작다면 : i 이전까지의 합은 소거하고 새로 i부터의 합을 구해나가는 것이 최댓값에 가까워지는 것이다.

따라서
dp.append(max(dp_sum[i-1] + dp_sum[i], dp_sum[i])
의 값이 dp_sum 리스트에 하나씩 추가되어 최종적으로
print(max(sum[i])의 값을 출력하면 된다.

## 점화식
```python
dp = list(map(int, input().split()))
sum = [dp[0]]
for i in range (n-1):
    sum.append(max(sum[i] + dp[i+1], dp[i+1]))
```

여기서 sum 리스트는 dp 리스트에 주어질 10개 숫자들의 합 리스트에 대한 것으로 sum[0]은 dp[0]값 혼자만의 값이기 때문에 sum=[dp[0]]이다.

<br>

## 풀이

```python
n = int(input())
dp = list(map(int, input().split()))
sum = [dp[0]]
for i in range (n-1):
    sum.append(max(sum[i] + dp[i+1], dp[i+1]))
print(max(sum))
```

풀이 과정
```python
# 풀이
# m = -5, +2, -4, +3, +6, -4 , ...
# i = 0
sum.append(max(sum[0] +m[0+1], m[0+1]))
sum.append(max(-5 + (+2), +2)
sum.append(max(-3, +2)) # sum = [-5, +2]

# i = 1
sum.append(max(sum[1) + m[1+1], m[1+1])
sum.append(max(+2 +(-4), -4))
sum.append(max(-2, -4)) # sum = [-5, +2, -2]

# i = 2
sum.append(max(sum[2] + m[2+1], m[2+1]))
sum.append(max(-2 + (+3)), +3)
sum.append(max(+1, +3)) # sum = [-5, +2, -2, +3]

# i = 3
sum.append(max(sum[3] + m[3+1], m[3+1))
sum.append(max(+3 + (+6), +6))
sum.append(max(+9, +3)) # sum = [-5, +2, -2, +3, +9]

# 이런식으로 sum 리스트가 채워진다. (0번째부터 n-1번째 까지 진행 / 총 횟수 = n번)
# 그 중에서 가장 최대값을 Print 한다.
```


<br>
<br>

# 9461 - Python
![](https://images.velog.io/images/c_hyun403/post/da7b4884-8bbc-4bdc-bfb6-655f5e1ba0e3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.48.44.png)![](https://images.velog.io/images/c_hyun403/post/9055c882-e610-4e38-adf6-bf9a01fbbee1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.48.51.png)

삼각형의 순서대로 변의 길이만 나열해보면
[1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12 ...]
이다. 대부분의 사람들이 i 번째 값이 [i-1] + [i-5] 값이라고 하는데 내가보기엔 i 번째 값 = [i-2] + [i-3] 과도 같다. 하지만!!!! 그림과 비교하여 논리적으로 판단을 해보면..
예를들어 변의 길이가 7인 삼각형의 경우 i-1 번째 변의 길이와 i-5번째 변의 길이의 합니다.
따라서 [i] = [i-1] + [i-5] 으로 점화식을 만든다.
또한 이 경의 5번째 까지 변의 길이가 제시되어야 식이 성립하므로 dp = [1, 1, 1, 2, 2]임을 명시해 주어야 한다.

## 점화식
```python
dp = [1, 1, 1, 2, 2]
if N > 5:
    for j in range(5, N):
        dp.append(dp[j-1] + dp[j-5])
````

<br>

## 풀이
```python
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [1, 1, 1, 2, 2]
    if N > 5:
        for j in range(5, N):
            dp.append(dp[j-1] + dp[j-5])
    print(dp[N-1])
```

<br>
<br>

### 이해 안되는 부분 1...
애초에 삼각형이 배치되는 과정이 위 예시 방법대로 **고정** 이라면 괜찮지만. 삼각형을 쌓아나가는 과정이 애초부터 위와 다르다면 식은 완전히 달라진다.
이건 문제를 꼬아 생각한 탓이라고 본다.

<br>

### 이해 안되는 부분 2...
코드중에서
dp 리스트의 위치에 따라 값이 완전히 다르게 나온다.
```python
T = int(input())
dp = [1, 1, 1, 2, 2]
for _ in range(T):
    N = int(input())
    if N > 5:
        for j in range(5, N):
            dp.append(dp[j-1] + dp[j-5])
    print(dp[N-1])
````
위 코드처럼 dp 리스트를 for 문 밖에 두면 12를 입력했을때 9의 값이 나온다. (6을 입력하면 똑같이 3으로 나온다.)
왜.. 그런지는 아직 파악 못했다...