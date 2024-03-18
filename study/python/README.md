# Generator
- 함수가 호출될때 반환되는 Iterator의 일종
- iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함
<br>
> **Iterator?** Java 의 컬렉션 프레임워크 (JCF)에서 컬렉션에 저장되어 있는 요소들을 읽어오는 방법을 표준화한 것으로
Iterator는 `반복자`로서 **객체 지향적 프로그래밍에서 배열이나 그와 유사한 자료구조의 내부요소를 순회하는 객체**이다.

### 다른 Iterable 객체와 차이점
#### 1. 메모리 관점
List나 Set, Dict는 모두 Iterable 하다. 하지만 모든 값을 메모리에 담고 있다. 이와 달리 제너레이터는 yeild 표현식을 통해 yeild 될때만 메모리를 차지한다.

### - 표현식
````python
import sys
a = [i for i in range(100000)]
>>> sys.getsizeof(a)
824472
b = (i for i in range(100000))
>>> sys.getsizeof(b)
128
````
