from matplotlib import pyplot
import numpy

x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint=True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
pyplot.figure(figsize=(11, 7))

pyplot.plot(x, y_sin, color='blue', linewidth=2.0)
pyplot.plot(x, y_cos, color='red', linewidth=2.0)

pyplot.xlim(x.min() * 1.2, x.max() * 1.2)
pyplot.ylim(y_sin.min() * 1.2, y_sin.max() * 1.2)

# x軸の目盛設定．リストを与える
pyplot.xticks([-numpy.pi * 2, -numpy.pi, 0, numpy.pi, numpy.pi * 2])
# y軸の目盛設定．リストを与える
pyplot.yticks([-1, -0.5, 0, 0.5, 1])

pyplot.show()
