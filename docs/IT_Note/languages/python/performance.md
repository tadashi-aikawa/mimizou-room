# [Python] パフォーマンス


パフォーマンス測定
------------------

### 実行時間

`timeit`を使う。戻り値に実行時間(秒)が返却される。

```python
import timeit


def measure_operations():
    # do something...


# 第1引数に計測するfunction
# 第2引数に試行回数
print(timeit.timeit(measure_operations, number=100))
```



### メモリ使用量

[memory_profiler]を使う。

[memory_profiler]: https://pypi.org/project/memory-profiler/

以下を実行すると各行での使用メモリとメモリ増加量が表示される。

```python
from memory_profiler import profile


@profile
def measure_operations():
    # do something...


measure_operations()
```

matplotlibを使うとメモリ使用量をグラフ化することができるらしい..

{{refer("https://blog.amedama.jp/entry/2018/02/04/001950")}}
