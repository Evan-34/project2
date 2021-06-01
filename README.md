# Project 2: # Project 1:  2-bit Histroy Predictor
使用python寫的簡單版 2-bit Histroy Predictor，即低分版input，
只有做一個2-bit History Predictor能處理以上的序列
會依序output 2-bit History和預測正確與否，最後再output整個的預測數據
## input
```
TTTTNNTNTNTNTNTNT
```

## output
```
incorrect
['00', 'WN', 'SN', 'SN', 'SN']
incorrect
['01', 'WN', 'WN', 'SN', 'SN']
incorrect
['11', 'WN', 'WN', 'SN', 'WN']
incorrect
['11', 'WN', 'WN', 'SN', 'WT']
incorrect
['11', 'WN', 'WN', 'SN', 'WN']
correct
['10', 'WN', 'WN', 'SN', 'WN']
incorrect
['00', 'WT', 'WN', 'SN', 'WN']
correct
['01', 'WT', 'SN', 'SN', 'WN']
incorrect
['10', 'WT', 'SN', 'WN', 'WN']
correct
['01', 'WT', 'SN', 'WN', 'WN']
incorrect
['10', 'WT', 'SN', 'WT', 'WN']
correct
['01', 'WT', 'SN', 'WT', 'WN']
correct
['10', 'WT', 'SN', 'ST', 'WN']
correct
['01', 'WT', 'SN', 'ST', 'WN']
correct
['10', 'WT', 'SN', 'ST', 'WN']
correct
['01', 'WT', 'SN', 'ST', 'WN']
correct
['10', 'WT', 'SN', 'ST', 'WN']
['N', 'N', 'N', 'N', 'N', 'T', 'N', 'T', 'N', 'T', 'N', 'T', 'T', 'T', 'T', 'T', 'T']

Process finished with exit code 0


```
