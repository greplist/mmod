# -*- coding: utf-8 -*-


def MKM(count, n=30, k=123456789, A0=2):
    m = 2**n
    A = list()
    A.append(A0)
    for i in xrange(count):
        A.append((k*A[i]) % m)

    z = [A[i] / float(m) for i in xrange(1, len(A))]
    return z


def test_simple(P=0.2, count=10000):
    X = MKM(count)
    n = sum([1 if x <= P else 0 for x in X])
    print('Иммитация простого события: Произошло: {} Не проихошло: {} Теор.P = {} Экспер.P = {}'.format(
                n, len(X) - n, P, n * 1.0 / len(X)))
    print('')


def test_complex(PA=0.6, PB=0.7, count=10000):
    X1 = MKM(count)
    X2 = MKM(count, A0=25325)

    A_B, notA_B, A_notB, notA_notB = 0, 0, 0, 0
    for a, b in zip(X1, X2):
        if a <= PA and b <= PB:
            A_B += 1
        elif a > PA and b <= PB:
            notA_B += 1
        elif a <= PA and b > PB:
            A_notB += 1
        elif a > PA and b > PB:
            notA_notB += 1

    print('Иммитация сложного события P(A) = {} и P(B) = {}:'.format(PA, PB))
    print('A и B: произошло {} в процентах {}% Теор {}%'.format(A_B, A_B * 100.0 / count, PA*PB*100.0))
    print('not A и B: произошло {} в процентах {}% Теор {}%'.format(notA_B, notA_B * 100.0 / count, (1 - PA)*PB*100))
    print('A и not B: произошло {} в процентах {}% Teop {}%'.format(A_notB, A_notB * 100.0 / count, PA*(1 - PB)*100))
    print('not A и not B: произошло {} в процентах {}% Teop {}%'.format(notA_notB, notA_notB * 100.0 / count, (1 - PA)*(1 - PB)*100))
    print('')


def test_dependent_complex(PA=0.6, PB=0.5, PBA=0.4, count=10000):
    X1 = MKM(count)
    X2 = MKM(count, A0=25325)

    PBnotA = (PB - PBA * PA) / (1 - PA)

    A_B, notA_B, A_notB, notA_notB = 0, 0, 0, 0
    for a, b in zip(X1, X2):
        if a <= PA and b <= PBA:
            A_B += 1
        elif a > PA and b <= PBnotA:
            notA_B += 1
        elif a <= PA and b > PBA:
            A_notB += 1
        elif a > PA and b > PBnotA:
            notA_notB += 1

    print('Иммитация зависимого сложного события P(A) = {} P(B) = {} P(B/A) = {}:'.format(PA, PB, PBA))
    print('A и B: произошло {} в процентах {}% Теор {}%'.format(A_B, A_B * 100.0 / count, PA*PBA*100.0))
    print('not A и B: произошло {} в процентах {}% Теор {}%'.format(notA_B, notA_B * 100.0 / count, (1 - PA)*PBnotA*100))
    print('A и not B: произошло {} в процентах {}% Teop {}%'.format(A_notB, A_notB * 100.0 / count, PA*(1 - PBA)*100))
    print('not A и not B: произошло {} в процентах {}% Teop {}%'.format(notA_notB, notA_notB * 100.0 / count, (1 - PA)*(1 - PBnotA)*100))
    print('')


def test_full_group(P=[0.05, 0.45, 0.5], count=10000):
    X = MKM(count)

    P = list(P) + [1.1]

    counters = [0] * len(P)
    for x in X:
        pred = 0
        for i, p in enumerate(P):
            if pred <= x and x < p:
                counters[i] += 1

    print('Иммитация полной группы событий:')
    for i, p in enumerate(P[:-1]):
        print('Событие №{}: Кол-во {} в процентах {}% Теорет. {}%'.format(
                i, counters[i], counters[i] * 100.0 / count, p * 100.0))
    print('')


if __name__ == '__main__':
    test_simple()
    test_complex()
    test_dependent_complex()
    test_full_group()
