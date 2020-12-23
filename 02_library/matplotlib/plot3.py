from matplotlib import pyplot
import numpy
x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint=True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
pyplot.figure(figsize=(11, 7))
# pyplot.plot(x, y_sin)
# pyplot.plot(x, y_cos)
pyplot.plot(x, y_sin, color='blue', linewidth=2.0)
pyplot.plot(x, y_cos, color='red', linewidth=2.0)
pyplot.show()
