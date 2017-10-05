import math
import pylab

from scipy.stats import norm


def M(nums):
    return sum(nums) * 1.0 / len(nums)


def D(nums):
    nlen, mnums = len(nums), M(nums)
    return sum([nums[i]**2 - mnums**2 for i in xrange(nlen)]) * 1.0 / nlen


def MKM(count, n=30, k=123456789, A0=2):
    m = 2**n
    A = list()
    A.append(A0)
    for i in xrange(count):
        A.append((k*A[i]) % m)

    z = [A[i] / float(m) for i in xrange(1, len(A))]
    return z


def exp_test(count):
    Y = list([norm.ppf(x) for x in MKM(count)])
    MY, TMY, DY, TDY = M(Y), 0.0, D(Y), norm.var()
    pylab.title('{} numbers. M = {:.4} TM = {:.4} D = {:.4} TD = {:.4}'.format(count, MY, TMY, DY, TDY))
    pylab.hist(Y, normed=1)

    X = list([x * 0.01 for x in xrange(-500, 500)])
    TY = list([norm.pdf(x) for x in X])
    pylab.plot(X, TY)

    pylab.show()

    # lambda(0.05) = 0.89
    F = [i / float(y) for i, y in enumerate(Y)]
    TF = [norm.cdf(x) for x in X]
    pylab.title('kolmogorov: must be {} < 0.86'.format(1 / math.sqrt(count) * max([abs(f - ft) for f, ft in zip(F, TF)])))

    pylab.show()


# def kolmogorov():
#     F1_teor = [1 - math.e ** (-l*y1[i]) for i in xrange(len(y1))]
#     F2_teor = [1 - math.e ** (-l*y2[i]) for i in xrange(len(y2))]
#     print math.sqrt(n)*max(abs(F2[i] - F2_teor[i]) for i in xrange(len(y2)))


if __name__ == '__main__':
    exp_test(10000)
