# Pandas

- Numpy 기반 파이썬 데이터 처리 라이브러리.
- import pandas as pd

 

# Series

- 1차원 배열의 각 값(values)에 대응되는 인덱스(index)로 된 구조.
- 각 값에 연산이 가능
- .index() : range 값이 있는 객체로, index 범위값만 반환하는 함수
- 딕셔너리, 시리즈 차이점 : 딕셔너리는 순서X, 시리즈 O

 

# DataFrame

- 가로:columns, 세로: index 로 구성 (시리즈로 구성된 표)
- Dictionay, List , numpy등을 값으로 처리 가능
- 동일한 index & column을 가진 데이터프레임끼리 연산가능

```python
pd.DataFrame(#객체명)
```

 

# Pandas_import & export

### 데이터 파일 가져오기_import

- read_확장자(‘파일명’)

```python
pd.read_csv(‘sample.csv’)
pd.read_txt(‘sample.txt’)
pd.read_excel(‘sample.xlsx’)
```

- head() : 상위 5개 자료를 가지고온다.

 

### 데이터 파일 내보내기_export

- .to_확장자(‘파일명’)

```python
df.to_csv(‘sample.csv’)
df.to_txt(‘sample.txt’)
df.to_excel(‘sample.xlsx’)
```

