import math
import numpy
import pylab
import scipy.stats


def MKM(count, n=30, k=123456789, A0=2):
    m = 2**n
    A = list()
    A.append(A0)
    for i in xrange(count):
        A.append((k*A[i]) % m)

    z = [A[i] / float(m) for i in xrange(1, len(A))]
    return z

def plot_hist():
    l = 1.5
    pylab.figure(figsize = (24, 6))
    x_min = 0.0
    x_max = 6.0
    n = 100
    h = (x_max - x_min) / n
    x  = [i*h for i in xrange(n)]
    y = [l*(math.e ** (-l*x[i])) for i in xrange(len(x))]

    pylab.subplot(1, 2, 1)
    x1 = MKM(100)
    y1 = [-1.0*(1.0 / l)*math.log(1 - x1[i]) for i in xrange(len(x1))]
    pylab.hist(y1, normed=1)
    M1 = sum(y1) / len(y1)
    D1 = sum([y1[i]**2 - M1**2 for i in  xrange(len(y1))]) / len(y1)
    pylab.title('{0} numbers. M = {1}. D = {2}'.format(len(y1), M1, D1))
    pylab.plot(x, y)

    pylab.subplot(1, 2, 2)
    x2 = MKM(10000)
    y2 = [-1.0*(1.0 / l)*math.log(1 - x2[i]) for i in xrange(len(x2))]
    pylab.hist(y2, normed=1)
    M2 = sum(y2) / len(y2)
    D2 = sum([y2[i]**2 - M2**2 for i in  xrange(len(y2))]) / len(y2)
    pylab.title('{0} numbers. M = {1}. D = {2}'.format(len(y2), M2, D2))
    pylab.plot(x, y)

    pylab.show()


def plot_func():
    pylab.figure(figsize = (24, 6))
    F = [1 - math.e ** (-l*x[i]) for i in xrange(len(x))]

    pylab.subplot(1, 2, 1)
    y1.sort()
    F1 = [i / float(len(y1)) for i in xrange(len(y1))]
    pylab.title("exponential function with parameter lambda : {0} and volume sample : {1}".format(l, len(y1)))
    pylab.plot(y1, F1)
    pylab.plot(x, F)

    pylab.subplot(1, 2, 2)
    y2.sort()
    F2 =[i / float(len(y2)) for i in xrange(len(y2))]
    pylab.title("exponential function with parameter lambda : {0} and volume sample : {1}".format(l, len(y2)))
    pylab.plot(y2, F2)
    pylab.plot(x, F)
    pylab.show()


def kolmogorov():
    F1_teor = [1 - math.e ** (-l*y1[i]) for i in xrange(len(y1))]
    F2_teor = [1 - math.e ** (-l*y2[i]) for i in xrange(len(y2))]
    print math.sqrt(n)*max(abs(F2[i] - F2_teor[i]) for i in xrange(len(y2)))


if __name__ == '__main__':
    plot_hist()
    plot_func()
    kolmogorov()
