import pandas
import numpy
import matplotlib
numpy.random.seed(42)
# 10行5列の配列（要素は乱数）を作る
data = numpy.random.randn(10, 5)
print(data)

# dataを要素とするDataFrameを作る
df = pandas.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])
print(df)
# 先頭3行を取得する
print(df.head(3))

# 後尾３行を取得する
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df['C'])
# 2行目から5行目を取得する
print(df[1:5])
# A, B, Eの全行を取得する
print(df.loc[:, ['A', 'B', 'E']])
print(df.loc[1:4, ['A', 'B', 'E']])
print(df.iloc[3])

# 2から3行目、2から3列目
print(df.iloc[1:3, 1:3])
mask = (df['A'] >= 0)
print(mask)
print(df[mask])
print(df[df['A'] >= 0])
print(df[df >= 0])

# mean() メソッドは平均を求めます。
print(df.mean())

# axis をパラメータとして与えることで平均を取る方向を指定することができます。
print(df.mean(axis=1))


# sum() メソッドは和を求めます。
print(df.sum())


# sum() メソッドも axis を与えることで和を求める方向を指定することができます。
print(df.sum(axis=1))
