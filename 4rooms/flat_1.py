# -*- coding: utf-8 -*-

# python modules
import time
import csv
# 3rd part modules
import constraint


# assign a Problem
problem = constraint.Problem()

# assign variables

x_0 = 2 # Прихожая
x_1 = 4 # Зал
x_2 = 2 # Сан узел
x_3 = 3 # Кухня

S_max = 54
S_min = 48

k = 3 / 4.0

# Прихожая
rd_0_smin = 4.0
rd_0_smax = 8.0
rd_0_lmin = x_0 * 10
rd_0_lmax = int(rd_0_smax * 100 / float(rd_0_lmin))
rd_0_k = k

r_0_sides = []
a = rd_0_lmin
while a <= rd_0_lmax:
    r_0_sides.append(a / 10.0)
    a += a * 0.25


# Зал
rd_1_smin = 8.0
rd_1_smax = 20.0
rd_1_lmin = x_1 * 10
rd_1_lmax = int(rd_1_smax * 100 / float(rd_1_lmin))
rd_1_k = k

r_1_sides = []
a = rd_1_lmin
while a <= rd_1_lmax:
    r_1_sides.append(a / 10.0)
    a += a * 0.25

# Сан узел
rd_2_smin = 4.0
rd_2_smax = 8.0
rd_2_lmin = x_2 * 10
rd_2_lmax = int(rd_2_smax * 100 / float(rd_2_lmin))
rd_2_k = k

r_2_sides = []
a = rd_2_lmin
while a <= rd_2_lmax:
    r_2_sides.append(a / 10.0)
    a += a * 0.25

# Кухня
rd_3_smin = 8.0
rd_3_smax = 20.0
rd_3_lmin = x_3 * 10
rd_3_lmax = int(rd_3_smax * 100 / float(rd_3_lmin))
rd_3_k = k

r_3_sides = []
a = rd_3_lmin
while a <= rd_3_lmax:
    r_3_sides.append(a / 10.0)
    a += a * 0.25


# rooms squares, sides
rd_0 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_0_sides for j in r_0_sides
        if (i / j >= rd_0_k and j / i >= rd_0_k) and (rd_0_smin <= i * j <= rd_0_smax)]
rd_1 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_1_sides for j in r_1_sides
        if (i / j >= rd_1_k and j / i >= rd_1_k) and (rd_1_smin <= i * j <= rd_1_smax)]
rd_2 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_2_sides for j in r_2_sides
        if (i / j >= rd_2_k and j / i >= rd_2_k) and (rd_2_smin <= i * j <= rd_2_smax)]
rd_3 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_3_sides for j in r_3_sides
        if (i / j >= rd_3_k and j / i >= rd_3_k) and (rd_3_smin <= i * j <= rd_3_smax)]

print "DEBUG: Number of squares for r_0\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_0), min(rd_0), max(rd_0))
print '\tSides:\t', r_0_sides, '\n'
print "DEBUG: Number of squares for r_1\t {}\t\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_1), min(rd_1), max(rd_1))
print '\tSides:\t', r_1_sides, '\n'
print "DEBUG: Number of squares for r_2\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_2), min(rd_2), max(rd_2))
print '\tSides:\t', r_2_sides, '\n'
print "DEBUG: Number of squares for r_3\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_3), min(rd_3), max(rd_3))
print '\tSides:\t', r_3_sides, '\n'


# assign constraint variables
problem.addVariable("r_0",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_4'} for i in rd_0])
problem.addVariable("r_1",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_4'} for i in rd_1])
problem.addVariable("r_2",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_3'} for i in rd_2])
problem.addVariable("r_3",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': ['r_2', 'r_4']} for i in rd_3])

problem.addConstraint(lambda r_0, r_1, r_2, r_3:
                      S_min < sum([r_0['sq'], r_1['sq'], r_2['sq'], r_3['sq']]) < S_max,
                      ['r_0', 'r_1', 'r_2', 'r_3'])
# problem.addConstraint(lambda r_0, r_1:
#                       r_0['a'] - 0.3 == r_1['a'],
#                       ['r_0', 'r_1'])
# problem.addConstraint(lambda r_0, r_2:
#                       r_0['b'] + 0.2 == r_2['b'],
#                       ['r_0', 'r_2'])

start = time.time()
solutions = problem.getSolutions()
finish = time.time()

solutions_number = len(solutions)
print ' DEBUG: Number of Solutions\t{}\t\tTime for Searching\t{} seconds.\n'.format(solutions_number, finish - start)


with open('rooms_a_b.csv', 'w') as csvfile:
    fieldnames = ['r_0_a', 'r_0_b', 'r_1_a', 'r_1_b', 'r_2_a', 'r_2_b', 'r_3_a', 'r_3_b']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for sol in solutions:
        out = {}
        for k, v in sol.items():
            out["{}_a".format(k)] = v['a']
            out["{}_b".format(k)] = v['b']
        writer.writerow(out)
