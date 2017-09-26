# -*- coding: utf-8 -*-

import pylab
from math import sqrt


def M(nums):
    return sum(nums) * 1.0 / len(nums)


def D(nums):
    nlen, mnums = len(nums), M(nums)
    return sum([nums[i]**2 - mnums**2 for i in xrange(nlen)]) * 1.0 / nlen


def correlation(nums, step=3):
    npairs = len(nums) - step
    X, Y = nums[:npairs], nums[step:]
    XY = list([X[i] * Y[i] for i in xrange(npairs)])
    return (M(XY) - M(X) * M(Y)) / sqrt(D(X) * D(Y))


def MKM(count, n=30, k=123456789, A0=2):
    m = 2**n
    A = list()
    A.append(A0)
    for i in xrange(count):
        A.append((k*A[i]) % m)

    z = [A[i] / float(m) for i in xrange(1, len(A))]
    return z


def MSK(count, first=1994):
    def next(number):
        number_str = str(number**2)
        len_str_number = len(number_str)
        number_str = '0' * (8 - len_str_number) + number_str
        number = int(number_str[2:6])
        return number

    nums = [first]

    pred = first
    for i in xrange(1, count):
        new = next(pred)
        nums.append(new)
        pred = new

    return list([num / float(9999) for num in nums])


class Figure(object):
    def __init__(self):
        pylab.figure(figsize=(24, 6))

    def plot(self, nums, i):
        print(nums[:10])
        pylab.subplot(1, 2, i)
        pylab.hist(nums, normed=1)
        pylab.title('{} numbers. M = {}. D = {}. K = {}'.format(len(nums), M(nums), D(nums), correlation(nums)))

    def show(self):
        pylab.show()


def test(method):
    n_100 = method(100)
    n_10000 = method(10000)

    # Тест равномерности
    figure = Figure()
    figure.plot(n_100, 1)
    figure.plot(n_10000, 2)
    figure.show()


if __name__ == '__main__':
    test(MSK)
    test(MKM)
