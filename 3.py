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


def build_F(X, Y):
    N = [0] * len(X)
    for i, x in enumerate(X):
        N[i] = sum([1 if y <= x else 0 for y in Y])

    count = len(Y)
    return list([n * 1.0 / count for n in N])


def exp_test(count):
    Y = list(([norm.ppf(x) for x in MKM(count)]))
    MY, TMY, DY, TDY = M(Y), 0.0, D(Y), norm.var()
    pylab.title('{} numbers. M = {:.4} TM = {:.4} D = {:.4} TD = {:.4}'.format(count, MY, TMY, DY, TDY))
    pylab.hist(Y, normed=1)

    X = list([x * 0.01 for x in xrange(-400, 400)])
    TY = list([norm.pdf(x) for x in X])
    pylab.plot(X, TY)

    pylab.show()

    F = build_F(X, Y)
    TF = [norm.cdf(x) for x in X]

    max_delta = max([abs(f - ft) for f, ft in zip(F, TF)])
    sigma = math.sqrt(count) * max_delta
    pylab.title('kolmogorov: max delta = {:.4} sigma = {:.4} < 0.86'.format(max_delta, sigma))
    pylab.plot(X, F)
    pylab.plot(X, TF)

    pylab.show()


if __name__ == '__main__':
    exp_test(1000)
