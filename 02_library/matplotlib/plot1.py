from matplotlib import pyplot
import numpy

x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint=True)
y_sin = numpy.sin(x)
pyplot.plot(x, y_sin)
pyplot.show()
