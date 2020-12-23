from matplotlib import pyplot
import numpy
x = numpy.linspace(-numpy.pi * 2, numpy.pi * 2, 1024, endpoint=True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
pyplot.figure(figsize=(11, 7))
pyplot.plot(x, y_sin, color='blue', linewidth=2.0, label=r'$\sin(x)$')
pyplot.plot(x, y_cos, color='red', linewidth=2.0, label=r'$\cos(x)$')
pyplot.xlim(x.min() * 1.2, x.max() * 1.2)
pyplot.ylim(y_sin.min() * 1.2, y_sin.max() * 1.2)
pyplot.xticks([-numpy.pi * 2, -numpy.pi, 0, numpy.pi, numpy.pi * 2],
              [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
pyplot.yticks([-1, -0.5, 0, 0.5, 1], [r'$-1.0$',
                                      r'$-0.5$', r'$0.0$', r'$0.5$', r'$1.0$'])
pyplot.legend()
# タイトル追加
pyplot.title('Test Plot')
pyplot.show()
