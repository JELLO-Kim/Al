# SQL문에서 String과 date 다루기
<br>

# String

## 문제1 : 특정 문자열 찾기
>
이름에 제시된 것이 포함된 data의 id, 이름, 중성화 유무 정보를 반환하세요.

### Sol1 : WHERE절에 OR로 조건잡기
```sql
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
WHERE
    NAME = "Lucy"
    OR name = "Ella"
    OR name = "Pickle"
    OR name = "Rogan"
    OR name = "Sabrina"
    OR name = "Mitty"
```
<br>

### Sol2 : WHERE 절에 IN으로 조건잡기
```sql
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
```
<br>

### Sol3 : 정규식 사용하기 (regexp)
```sql
SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
WHERE NAME REGEXP '^(Lucy|Ella|Pickle|Rogan|Sabrina|Mitty)$'
```
#### 주의!
정규식을 사용할때 양 끝에 ^와 &로 범위를 지정해 주어야 한다. <p>
그렇지 않으면 해당 단어가 **포함된** 단어를 찾기 때문에 정확하지 않다.

<br>

## 문제2 : 특정 단어가 "포함된" 값 찾기

>- 종류는 강아지만
>- 이름순으로 조회
>- 특정단어는 대소문자를 구분하지 않고 찾는다

<br>

### Sol1 : 정규식 사용하기
이전문제에서 활용한 정규식을 사용해보았다. <p>
정규식에서 잡은 것은 'EL' 이의 대소문자를 구분하지 않는다.
```sql
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE
    NAME REGEXP 'EL'
    AND
    ANIMAL_TYPE = 'DOG'
ORDER BY
    NAME ASC
```

<br>

### Sol2 : LIKE + %사용해 "포함된" 문자열 찾기 (대소문자 구분 불필요)

MySQL에서는 LIKE를 사용할 경우 해당 문자열의 **대소문자를 구분하지 않고 모두 조건으로 잡는다.**
```sql
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_INS
WHERE
    NAME LIKE '%EL%'
    AND
        ANIMAL_TYPE = 'Dog'
ORDER BY
    NAME ASC
```

<br>

## 문제3 : 특정 단어가 포함된 문자에 지정된 단어1로 표기하게하기 (아닐경우 지정된 단어2로 표기)

<br>

### Sol1 : IF() 사용하기

IF(조건, True일 경우, False일 경우)

```sql
SELECT
    ANIMAL_ID,
    NAME,
    IF(SEX_UPON_INTAKE LIKE 'Intake%', 'X', 'O')
FROM
    ANIMAL_INS
ORDER BY
    ANIMAL_ID
```

- 중성화에 해당하는 경우가 아닌 조건이 하나이므로 해당 조건에 대해서 IF문을 지정한다.
- Intake라는 단어가 있을 경우 'X', 없을 경우 'O'가 표기되도록 한다.

<br>

### Sol2 : IF() + 정규식 사용하기
```sql
SELECT  ANIMAL_ID,
        NAME,
        IF(SEX_UPON_INTAKE REGEXP 'Neutered|Spayed', 'O' , 'X') AS 중성화
FROM    ANIMAL_INS
```
기호 |는 OR을 의미한다 같은 string 기호 안에 처리해준다.

<br>



### Sol3 : CASE, ELSE 문 사용하기
python과는 달리 ELSE문이 아닌 **IF문을 생략**하고, 지정된 조건이 아닐 경우에 대해서 "ELSE"문을 사용할 수 있다.

```sql
SELECT
    ANIMAL_ID,
    NAME,
CASE WHEN SEX_UPON_INTAKE LIKE "Neutered%" THEN 'O'
WHEN SEX_UPON_INTAKE LIKE "Spayed%" THEN 'O'
ELSE 'X' END SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

#### CASE 사용법
```sql
CASE
    WHEN 조건1
        THEN 반환 값1
    WHEN 조건2
        THEN 반환 값2
    ELSE 위의 조건1, 2 모두 해당 안될 경우의 반환 값3
```

<br>
<br>

# -----------------------------------

<br>
<br>

# Date