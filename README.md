# mmod

1 работа
 Для каждого метода получить выборки разных размеров (например, 100, 1000, 10 000). Для каждой выборки построить гистограмму, посчитать матожидание, дисперсию, корреляцию (тест независимости).

2 работа
 Во всех имитациях сгенерировать выборки размером >= 1000. При имитации простого события вывести, сколько раз событие произошло, сколько раз не произошло (количество и % от общего числа), посчитать теоретические и экспериментальные матожидание и дисперсию. При имитации независимых и зависимых событий вывести, сколько раз произошли следующие события (количество и % от общего числа): A, B, A and B, A and !B, !A and B, !A and !B. При имитации полной группы событий вывести, сколько раз произошло каждое событие (количество и % от общего числа).

3 работа
 Выбираете какое-либо непрерывное распределение: нормальное, логнормальное, экспоненциальное и т.д. Генерируете выборку, рисуете гистограмму и плотность распределения на одном графике, считаете теоретические и экспериментальные матожидание и дисперсию, доверительные интервалы для матожидания и дисперсии. Считаете критерий согласия (Колмогорова или Пирсона), на основе которого делаете вывод, соответствует ли выборка данному распределению.

Так как для большинства распределений записать функцию распределения проблематично, воспользуйтесь какой-либо библиотекой для подсчета функции распределения. Например, можете воспользоваться python-библиотекой scipy, которая содержит функцию scipy.stats.norm.cdf для подсчета функции распределения, ppf - обратной функции распределения, pdf - плотности распределения (аналогично для других распределений).

4 работа
Все как сказано в задании, матожидание и дисперсия теоретические и экспериментальные, 2 гистограммы (одна для значений первой случайной величины, вторая для значений второй случайной величины).
