from matplotlib import pyplot
import numpy

x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint=True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
pyplot.figure(figsize=(11, 7))
pyplot.plot(x, y_sin, color='blue', linewidth=2.0)
pyplot.plot(x, y_cos, color='red', linewidth=2.0)
# x軸の最小値、最大値を、xの最小値、最大値の1.2倍とする
pyplot.xlim(x.min() * 1.2, x.max() * 1.2)
# y軸の最小値、最大値を、y_sinの最小値、最大値の1.2倍とする
pyplot.ylim(y_sin.min() * 1.2, y_sin.max() * 1.2)
pyplot.show()
