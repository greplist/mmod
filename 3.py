import math
import pylab

from scipy.stats import norm


def M(nums):
    return sum(nums) * 1.0 / len(nums)


def M_with_interval(X):
    m = M(X)

    # y = 0.99 & n > 100 (koeff Studenta)
    t = 3.319
    s = math.sqrt(sum([(xi - m) ** 2 for xi in X]) * 1.0 / (len(X) - 1))
    delta = s * t / math.sqrt(len(X) - 1)

    return m - delta, m, m + delta


def D(nums):
    nlen, mnums = len(nums), M(nums)
    return sum([nums[i]**2 - mnums**2 for i in xrange(nlen)]) * 1.0 / nlen


def D_with_interval(X):
    m = M(X)

    xi2_minus, xi2_plus = 993.26, 897.36
    n_s_2 = sum([(xi - m) ** 2 for xi in X]) * 1.0 / (len(X) - 1) * len(X)

    return n_s_2 / xi2_minus, D(X), n_s_2 / xi2_plus


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
    TMY, TDY = 0.0, norm.var()
    M_min, MY, M_max = M_with_interval(Y)
    D_min, DY, D_max = D_with_interval(Y)
    pylab.title('N={}: {:.3}<= M <={:.3} (M={:.3} TM={:.3})\n {:.3}<= D <={:.3} (D={:.3} TD={:.3})'.format(
        count, M_min, M_max, MY, TMY, D_min, D_max, DY, TDY))
    pylab.hist(Y, normed=1)

    X = list([x * 0.01 for x in xrange(-400, 400)])
    TY = list([norm.pdf(x) for x in X])
    pylab.plot(X, TY)

    pylab.show()

    F = build_F(X, Y)
    TF = [norm.cdf(x) for x in X]

    # alpha = 0.01 & n = 1000
    max_sigma = 0.86

    max_delta = max([abs(f - ft) for f, ft in zip(F, TF)])
    sigma = math.sqrt(count) * max_delta
    pylab.title('kolmogorov: max delta = {:.4} sigma = {:.4} < {:.4}, viborka is {}'.format(
        max_delta, sigma, max_sigma, 'OK' if sigma < max_sigma else 'NOT OK'))
    pylab.plot(X, F)
    pylab.plot(X, TF)

    pylab.show()


if __name__ == '__main__':
    exp_test(1000)
