# SQL이란

SQL은 Structured Query Language(구조적 질의 언어)의 줄임말로, 관계형 데이터 베이스 시스템(RDBMS)에서 자료를 관리 및 처리하기 위해 설계된 언어

SQL은 1970년대에 IBM에서 최초 개발되었으며 관계형 모델이라는 이론에서 파생된 특징을 가지고 있는데, 현재SQL의 표준으로 ANSI SQL이 정립되었습니다. 각 DBMS프로그램에서 ANSI SQL을 기반으로 개발된 개별 SQL을 사용하며 서로 근소한 차이를 보입니다.



# SQL 문법의 종류

- DDL(data definition Language,데이터 정의 언어 )

  각 릴레이션을 정의하기 위한 언어(CREATE, ALTER, DROP...ETC)

- DML(Data manipulation Language, 데이터 조작 언어)
  데이터를 추가/수정/삭제하기 위한, 즉 데이터 관리를 위한 언어(SELCET,INSERT<UPDATE....ETC)

- DCL(Data Conteol Languate, 데이터 제어 언어)

  사용자 관리 및 사용자별로 릴레이션 또는 데이터를 관리하고 접근하는 권한을 다루기 위한 언어 (GRANT, REVOKE...ETC)



# SQL 언어적 특성

1. SQL은 대소문자를 구분하지 않는다.
   단, 서버환경이나 DBMS 종류에 따라 데이터베이스 또는 필드명에 대해 대소문자를 구분하기도 함
2. SQL 명령은 반드시 세미콜론(;)으로 끝난다.
3. 고유의 값은 따옴표(' ')로 감싸준다.
4. SQL에서 객체를 나타낼 떄는 백틱( `)으로 감싸준다.
5. 주석은 일종의 도움말로 주석처리된 문장은 프로그램에서 동작하지 않는다. 한줄 주석은 문장 앞에 --를 붙여서 사용한다.
6. 여러 줄 주석은  /* */으로 감싸준다.





# DBMS

DBMS란 DataBase Mangement System의 줄임말로, 컴퓨터에 저장된 데이터베이스를 관리해주는 소프트웨어를 지칭한다. 만약 데이터를 파일단위로 직접 관리한다면 수십여 건 정도는 각자 할 수 있지만 데이터 수가 증가하여 관리해야할 파일이 많아진다면 한계에 부딪히게 될것이다. 때문에 DBMS를 활용하여 데이터를 데이터베이스로 정리하여 좀 더 효율적으로 데이터를 통제하고 관리할 수 있다.



# 데이터 모델

현실 세계에 있는 다양한 데이터를 있는 그대로 컴퓨터의 데이터 베이스에 넣고 싶은 경우 어떻게 하면 될까요? 예를 들어 '고양이'라는 개체의 데이터를 데이터 베이스에 넣는다고 가정하면 다음과 같은 순서로 데이터 베이스를 구성할 수 있습니다.

1. 고양이의 무엇을 데이터로 취급할 것인지 결정합니다. 여기서는 고양이의 외향적 특징으로 데이터 베이스를 구성하고자 합니다.
2. 고양이의 외향적 특징을 데이터로 선별합니다. 예를 들어 '귀는 세모로 뾰족하게 2개 가지고 있다.', ' 4개의 발은 말랑한 발바닥과 날카로운 발톱으로 이루어져 있다' 와 같은 데이터입니다.
3. 데이터베이스에 적절한 구조를 사용하여 고양이의 부위별 특징을 저장합니다.

위와 같이 현실 세계의 데이터를 변환하여 컴퓨터 데이터 베이스에 저장하는 과정을 데이터 모델링이라고 하며, 특정 데이터를 선별 및 정리하는 과정을 추상화 라고 합니다. 또한, 데이터 모델링을 통해 데이터 사이의 관계와 그 흐름에 필요한 처리과정과 제약 조건등을 추상화 하여 표현한 개념적인 모형을 데이터 모델이라고 합니다. 예시를 통해 설명하자면, 위 과정중 2번에서 추상화를 진행하며, 2번과 3번 단계의 결과로 데이터 모델이 도출되는 것 입니다.



데이터 모델은 크게 '개념적 데이터 모델'과 '논리적 데이터 모델'로 나뉩니다.

|                    | 설명                                                         | 예시                                         |
| ------------------ | ------------------------------------------------------------ | -------------------------------------------- |
| 개념적 데이터 모델 | 현실 세계의 사용자가 이해할 수 있는 추상적인 구조로 표현한 모델 (정보모델이라고도 부름) | E-R모델<br />(개체-관계모델)                 |
| 논리적 데이터 모델 | 개념적 데이터 모델을 컴퓨터가 이해할 수 있도록 변환한 모델   | 관계형 데이터 모델, 계층 모델, 네트워크 모델 |

*일반 적으로 '데이터 모델'이라고 말하는 대부분의 모델은 논리적 데이터 모델을 지칭합니다. 대표적으로 계층형 데이터 모델, 네트워크형 데이터 모데르 관계형 데이터 모델, 객체 지향형 데이터 모델 등이 있으며, 현재 관계형 데이터 모델이 가장 선호되고 있습니다.



# E-R 모델

개체-관계 모델 이라고도 부르는 E-R모델은 데이터 구조를 설계하는 데 있어 각각의 요소를 개체(Entity)와 속성(Attritute), 관계(Realtion)로 나뉘어 기술하는 것을 뜻하며, 이를 다이어그램으로 표현한 것을 E-R 다이어그램이라고 부릅니다.



1. 개체(Entity)

   1. 개체는 저장할 가치가 있는 중요 데이터를 가진 사람이나 사물, 개념등으로 지정

      다른 개체와 구별되는 이름 및 고유한 속성, 인스턴스를 하나 이상 가지고 있다.

   2. E-R 다이어그램에서 개체는 사각형으로 표현

2. 속성(Attribute)

   1. 의미 있는 데이터의 가장 작은 논리적 단위인 속성은 개체 혹은 관계가 가진 고유 특성을 의미
   2. E-R 다이어그램에서 속성은 타원으로 표현

3. 관계(Relationshop)

   1. 관계는 개체와 개체 사이의 연관성 및 개체 집합 사이의 대응 관계, 즉 매핑을 의미
   2. E-R 다이어그램에서 마름모로 표현



### *E_R모델 예시

![E-R diagram](SQL%EC%9D%B4%EB%9E%80/An-ER-Diagram-illustrating-3-entities-Professors-Students-and-Courses-their.ppm)



# 관계 데이터 모델

데이터베이스 스키마:  데이터베이스에 저장할 수 있는 형태로 표현한 곤리 구조

1. 릴레이션(Relation)
   하나의 개체에 관한 데이터를 2차원 테이블 구조로 저장한 것
2. 속성(Attribute)
   테이블 각각의 열을 지칭하는 단어로 필드 혹은 칼럼 이라고 부른다.
3. 튜플(Tuple)
   테이블 각각의 행을 지칭한다. 레코드라고도 부른다.
4. 차수(Degree)
   테이블에서의 속성 총 개수를 의미한다.
5. 카디널리티(Cardinality)
   테이블에서의 튜플 총 개수를 의미한다.
6. 도메인(Domain)
   도메인이란 가각의 필드에 입력 가능한 값의 범위를 의미, 각 속성이 가질 수 있는 모든 값의 집합
7. 널(NULL)
   특정 속성값을 알지 못하거나 아직 값이 정해지지 않아 입력하지 못한 값을 NULL이라고 한다.
   NULL은 0 또는 공백과는 달리 어떠한 값도 없는 정보의 부재를 표현한다.



# 데이터 타입

데이터 모델을 설계할 때 각 필드에는 그 성격에 적합한 형태의 데이터를 저장해야한다. 여기서 데이터의 성격, 즉 자료의 형태를 결정하는 유형을 자료형이라 하며, DBMS마다 자료형의 명칭이 조금씩 다르다.

1. 숫자형

   | 명칭    | 자료유형 | 자료크기 | 참고                                          |
   | ------- | -------- | -------- | --------------------------------------------- |
   | INTEGER | 정수형   | 4byte    | 숫자표현                                      |
   | FLOAT   | 실수형   | 4byte    | 부동 소수형 데이터 타입, 고정 소수점 사용형태 |
   | NUMBER  | 숫자형   | 22byte   | 가변 길이 숫자 타입                           |

2. 문자형

   | 명칭    | 자료유형         | 자료크기       | 참고                                                         |
   | ------- | ---------------- | -------------- | ------------------------------------------------------------ |
   | CHAR    | 고정 길이 문자열 | 최대 255 byte  | 지정 길이보다 짧은 데이터 입력 시 나머지 공간은 공백으로 채운다 |
   | VARCHAR | 가변 길이 문자열 | 최대 65535byte | 지정 길이보다 짧은 데이터 입력 시 나머지 공간은 채우지 않는다 |

3. 날짜형

   | 명칭      | 자료유형  | 자료크기 | 참고                                       |
   | --------- | --------- | -------- | ------------------------------------------ |
   | DATE      | 일자      | 3byte    | 날짜(년도, 월, 일)형태의 기간 표현         |
   | TIME      | 시간      | 3byte    | 시간(시,분,초) 형태의 기간 표현            |
   | TIMESTAMP | 일자+시간 | 4byte    | 시스템 변경 시 자동으로 그 날짜와 시간저장 |

   