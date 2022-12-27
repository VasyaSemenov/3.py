from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand')

(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X+1))))
print(y[1000000] == Sm)
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[1000000], 1000000] == Average)

l = sorted([random.choice(range(1000000)) for i in range(100)])
(y['sum_rand'] == sum_(Z, for_each=Z)) <= Z.in_(l)
print(y['sum_rand'] == SumRand)
print("Median: ", (l[49] + l[50]) / 2)