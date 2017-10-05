import copy
import pylab


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


def resolve_index(PI, x):
    P = list([sum(PI[:i+1]) for i in range(len(PI))])

    pred = 0
    for i, p in enumerate(P):
        if pred <= x and x <= p:
            return i
        pred = p

    raise Exception("Unreacheble, may be x > 1? (x = {})".format(x))


def plot_xi(XI, A, PX):
    X = list([A[xi] for xi in XI])
    TX = list([p * a for p, a in zip(PX, A)])

    MX, TMX, DX, TDX = M(X), M(TX), D(X), D(TX)
    pylab.title('N={}: M={:.3} TM={:.3}\n D={:.3} TD={:.3}'.format(
        len(XI), MX, TMX, DX, TDX))
    pylab.hist(X, normed=1)
    pylab.show()


def test(P, A, B, count=10000):
    n, m = len(P), len(P[0])

    PX = list([sum(raw) for raw in P])
    PY = list([sum([P[i][j] for j in range(n)]) for i in range(m)])

    PY_X = copy.deepcopy(P)
    for i in range(len(P)):
        for j in range(len(P[i])):
            PY_X[i][j] = P[i][j] / PX[i]

    XI = list([resolve_index(PX, x) for x in MKM(count)])
    print(PY_X)
    print(XI)
    YI = list([resolve_index(PY_X[xi], y) for xi, y in zip(XI, MKM(count, k=321321321))])

    plot_xi(XI, A, PX)
    plot_xi(YI, B, PY)


if __name__ == '__main__':
    P = [
        [0.1, 0.1, 0.1],
        [0.1, 0.05, 0.25],
        [0.05, 0.2, 0.05],
    ]
    A = (10, 20, 30)
    B = (1, 2, 3)
    test(P, A, B)
