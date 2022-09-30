# Simple performance Test: Pandas vs List(builtin)
동일한 데이터 셋으로 동일한 결과를 만드는 두 가지 방법에 대해서 간단히 테스트를 해본다

- Pandas(DataFrame) 
- Python Builtin Function(list, map)

## DataSet
테스트에 사용할 데이터는 [mockaroo](https://www.mockaroo.com/)에서 준비하였다 

해당 사이트에서 다운빋을 수 있는 데이터 20만개로 제한되어 있다. 20만개를 그대로 복사하여 50만개를 맞추어서 진행하였다

- 테스트 데이터 [test_dataset.csv](test_dataset.csv)
- 데이터 개수별로 다음과 같이 순차적으로 진행: 100, 1000, 10,000, 50,000, 100,000, 200,000, 300,000, 400,000, 500,000

## Test
테스트는 두 가지 방법으로 진행하였다

### Filter
- 문자열 컬럼에서 dataframe으로 필터링 vs iterator를 사용하여 필터링 
- 숫자형 컬럼에서 dataframe으로 필터링 vs iterator를 사용하여 필터링

### Apply
- 문자열 컬럼에서 dataframe으로 apply 사용 vs iterator + map을 사용하여 변환
- 숫자형 컬럼에서 dataframe으로 apply 사용 vs iterator + map을 사용하여 변환


## Result
각 테스트 별로 최소 실행 시간을 기록하였다

원본 테스트 결과는 [filter_result.csv](filter_result.csv)와 [apply_result.csv](apply_result.csv)에서 확인할 수 있다

### Pandas vs Builtin List: Filter Performance


### Pandas vs Builtin List: Apply Performance


