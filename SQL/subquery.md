# 1. 특정 시간대의 갯수 파악하기

## 💡 문제
datetime 형태로 입력된 field값들 중 각 시간대의 data 갯수를 파악해 "특정 시간"대의 값만을 출력해야 한다.

<br>

### ⚙️ Sol1 : SUBSTRING() 사용하기
```sql
SELECT *
FROM (
    SELECT
    SUBSTRING(DATETIME, 12, 2) AS TIME,
    COUNT(*) AS "COUNT"
FROM
    ANIMAL_OUTS
GROUP BY
    SUBSTRING(DATETIME, 12, 2)
ORDER BY
    TIME
    ) AS cnt
WHERE
    TIME BETWEEN "09" AND "19"
```

첫번째 query = SELECT * <p>
두번째 query = sub query

#### 두번째 query
- substring()을 사용하였다. 그래서 datetime 타입으로 인해 yyyy-mm-dd hh:mm:ss 로 표기되던 형태에서 12번째 index 즉, 시간이 표기되기 시작하는 index로부터 2개길이만큼만 확인한다. (별칭 = TIME)
<br>

> **substring() ??**
>- substring(column 명, 시작 index, 지속 len)
>- substring() 혹은 substr() 이라고 표기한다.
>- 첫번째의 index는 1이다.

- GROUP BY로 시간에 대한것으로 묶은 후, COUNT 하여 각 시간마다의 갯수를 파악했다.
- ORDER BY로 시간별 오름차순으로 정렬해 주었다.
- 모든 subquery table은 그 별칭이 있어야 하므로 이후 사용되는 곳은 없지만 별칭을 cnt라고 지어주었다.

#### 첫번째 query
- subquery로 가져온 값 모두를 가져온다.
- WHERE절을 통해 그중에서 시간이 09 ~ 19 인것만 가져오게 한다.

### 🔥 아쉬운점
시간에 대한 값을 "문자열"로 가져왔기 때문에 9 가 아닌 09로 표시된다. 09에서 9를 없애기 위해 다음의 풀이법을 참고하였다.

<br>

### ⚙️ Sol2 : HOUR 사용하기

> ** MySQL의 함수 **
MySQL에 있는 여러 함수들 중 날짜에 관련된 함수들이 있다.
- YEAR : 연도 추출
- MONTH : 월 추출
- DAY : 일 추출 (DAYOFMONTH와 같은 함수이다)
- HOUR : 시 추출
- MINUTE : 분 추출
- SECOND : 초 추출

이중에서 사용할 것은 **HOUR** 함수이다.

```sql
SELECT
    HOUR(DATETIME),
    COUNT(DATETIME)
FROM
    ANIMAL_OUTS
WHERE
    HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY
    HOUR(DATETIME)
ORDER BY
    HOUR(DATETIME)
```
subquery를 사용하지 않고 하나의 query로 값을 불러올 수 있었다.

추가로 WHERE절이 아닌 GROUP BY절에서 HAVING을 사용해 조건을 잡을 수도 있다.
```sql
SELECT
    HOUR(DATETIME) AS HOUR,
    COUNT(DATETIME)
FROM
    ANIMAL_OUTS
GROUP BY
    HOUR(DATETIME) HAVING HOUR BETWEEN 9 AND 19
ORDER BY
    HOUR(DATETIME)
```

#### 주의!!
GROUP BY에서 HAVING절은 SELECT절에서 사용한 column의 별칭을 사용해야 했다.
원래 그렇진 않은걸로 알고있는데 HOUR함수를 통해 특정 데이터를 뽑아냈기 때문이라 생각한다. (가공 존재)

<br>
<br>

# ---------------------------------------------------------------

<br>
<br>

# 2. 없는 값으로 column 사용하기

### 💡 문제
주어진 시간대가 07 ~ 19까지만 있는 table 이지만 최종적으로 반환되는 값에는 0시부터 24시까지 포함되어야 한다. 각 시간대별의 data 갯수를 표기하라.

### ⚙️ Sol1 : NATURAL JOIN 활용하기
> **NATURAL JOIN**
서로 다른 두 테이블간에 동일한 이름, 타입을 사용하는 column이 존재할때 사용하는 JOIN이다.

```sql
SELECT HOUR, COUNT(S.HOUR) AS COUNT
FROM (   
    SELECT HOUR(DATETIME) AS HOUR
    FROM ANIMAL_OUTS
) AS S NATURAL RIGHT JOIN
((SELECT 0 as HOUR) UNION (SELECT 1) UNION (SELECT 2) UNION (SELECT 3) UNION (SELECT 4) UNION (SELECT 5) UNION (SELECT 6) UNION (SELECT 7) UNION (SELECT 8) UNION (SELECT 9) UNION (SELECT 10) UNION (SELECT 11) UNION (SELECT 12) UNION (SELECT 13) UNION (SELECT 14) UNION (SELECT 15) UNION (SELECT 16) UNION (SELECT 17) UNION (SELECT 18) UNION (SELECT 19) UNION (SELECT 20) UNION (SELECT 21) UNION (SELECT 22) UNION (SELECT 23)) as T
GROUP BY HOUR
ORDER BY HOUR
```

RECURSIVE로 가상의 테이블을 생성하지 않아 없는 값에대한 column을 직접 만들어준 경우이다. 0시부터 23시까지 해당하는 값 각각을 **UNION**으로 생성해준다.
- "ANIMAL_OUTS"의 시간에 대한 column에 값을 더하는 것이르모 **NATURAL JOIN**을 사용한다. 때문에 0부터 23까지 중 `HOUR(DATETIME)`으로 지정되는 값이 있을 경우 두개가 생성되지 않고 하나만 사용하게 된다.
- subquery로 생성된 모든 값은 그 별칭을 지정해 주어야 하므로 이후 사용되는 일이 없지만 NATURAL JOIN으로 생성된 값에도 별칭을 지어준다 (T)
- GROUP BY HOUR : 각 시간에 대한 값을 반환하도록 한다

<br>

### ⚙️ Sol2 : RECURSIVE 활용하기

MySQL에서 가상의 테이블을 만드는 방법이다.
```sql
WITH RECURSIVE 테이블명 AS(
    SELECT 초기값 AS 별칭1
        UNION ALL
        SELECT 별칭1 계산식 FROM 테이블명 WHERE 제어조건
    )
```
- 테이블명에 대해서 가상의 테이블을 만든다
- AS : 테이블이 성립되는 조건이 담긴다
- 초기값 : 해당 값의 처음 값을 지정한다
- UNION : 이후 지정되는 값들을 모두 더해준다
> ** UNION ?**

- 계산식 : 초기값으로 지정된 별칭1의 값을 이후 풀어나갈 계산식이다 (ex_ +1)
- FROM 테이블명 : 처음에 지정한 가상의 테이블을 지칭한다
- WHERE : 제어조건을 지정해준다. (ex_ 별칭1 < 10)


```sql
WITH RECURSIVE TIME AS(
    SELECT 0 AS h
        UNION ALL
        SELECT h+1 FROM TIME WHERE h < 23)

SELECT h, COUNT(HOUR(DATETIME)) AS 'COUNT'
FROM TIME LEFT JOIN ANIMAL_OUTS
ON (h=HOUR(DATETIME))
GROUP BY h
```
1. RECURSIVE를 사용해 column명이 h이고 table명이 TIME인 가상의 테이블을 생성한다.
2. 가상의 테이블의 새로운 h column은 0부터 23까지의 정수이다.
3. 가상의 테이블을 기준으로 주어진 "ANIMAL_OUTS"테이블을 JOIN한다. 이때의 기준은 동일한 시간대의 coulmn만 지정하는 것이다. (ON조건)
4. GROUP BY를 사용해 h column대로 값이 반환되도록 한다.
