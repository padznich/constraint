# -*- coding: utf-8 -*-

# python modules
import time
# 3rd part modules
import constraint


# assign a Problem
problem = constraint.Problem()

# assign variables

# Кухня
rd_0_smin = 9.0
rd_0_smax = 16.0
rd_0_lmin = 23
rd_0_lmax = int(rd_0_smax * 100 / float(rd_0_lmin))
rd_0_k = 1 / 3.0
r_0_sides = [i / 10.0 for i in range(rd_0_lmin, rd_0_lmax + 1, 5)]

# Санузел
rd_1_smin = 3.6
rd_1_smax = 4.5
rd_1_lmin = 15
rd_1_lmax = int(rd_1_smax * 100 / float(rd_1_lmin))
rd_1_k = 1 / 3.0
r_1_sides = [i / 10.0 for i in range(rd_1_lmin, rd_1_lmax + 1, 5)]

# Жилая комната
rd_2_smin = 14
rd_2_smax = 20
rd_2_lmin = 30
rd_2_lmax = int(rd_2_smax * 100 / float(rd_2_lmin))
rd_2_k = 1 / 2.0
r_2_sides = [i / 10.0 for i in range(rd_2_lmin, rd_2_lmax + 1, 5)]

# Прихожая
rd_3_smin = 3
rd_3_smax = 4.5
rd_3_lmin = 14
rd_3_lmax = int(rd_3_smax * 100 / float(rd_3_lmin))
rd_3_k = 1 / 3.0
r_3_sides = [i / 10.0 for i in range(rd_3_lmin, rd_3_lmax + 1, 5)]

# *Коридор
rd_4_smin = 1.5
rd_4_smax = 8
rd_4_lmin = 12
rd_4_lmax = int(rd_4_smax * 100 / float(rd_4_lmin))
r_4_sides = [i / 10.0 for i in range(rd_4_lmin, rd_4_lmax + 1, 5)]

# *Гардероб
rd_5_smin = 1
rd_5_smax = 2
rd_5_lmin = 5
rd_5_lmax = int(rd_5_smax * 100 / float(rd_5_lmin))
r_5_sides = [i / 10.0 for i in range(rd_5_lmin, rd_5_lmax + 1, 5)]
rd_5_k = 1 / 3.0

# rooms squares, sides
rd_0 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_0_sides for j in r_0_sides
        if (i / j >= rd_0_k or j / i >= rd_0_k) and (rd_0_smin <= i * j <= rd_0_smax)]
rd_1 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_1_sides for j in r_1_sides
        if (i / j >= rd_1_k or j / i >= rd_1_k) and (rd_1_smin <= i * j <= rd_1_smax)]
rd_2 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_2_sides for j in r_2_sides
        if (i / j >= rd_2_k or j / i >= rd_2_k) and (rd_2_smin <= i * j <= rd_2_smax)]
rd_3 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_3_sides for j in r_3_sides
        if (i / j >= rd_3_k or j / i >= rd_3_k) and (rd_3_smin <= i * j <= rd_3_smax)]
rd_4 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_4_sides for j in r_4_sides
        if (rd_4_smin <= i * j <= rd_4_smax)]
rd_5 = [{"sq": round(i * j, 2), 'a': i, 'b': j} for i in r_5_sides for j in r_5_sides
        if (rd_5_smin <= i * j <= rd_5_smax) or i * j == 0] + [{"sq": 0, "a": 0, "b": 0}]
print "DEBUG: Number of squares for r_0\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_0), min(rd_0), max(rd_0))
print '\tSides:\t', r_0_sides, '\n'
print "DEBUG: Number of squares for r_1\t {}\t\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_1), min(rd_1), max(rd_1))
print '\tSides:\t', r_1_sides, '\n'
print "DEBUG: Number of squares for r_2\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_2), min(rd_2), max(rd_2))
print '\tSides:\t', r_2_sides, '\n'
print "DEBUG: Number of squares for r_3\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_3), min(rd_3), max(rd_3))
print '\tSides:\t', r_3_sides, '\n'
print "DEBUG: Number of squares for r_4\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_4), min(rd_4), max(rd_4))
print '\tSides:\t', r_4_sides, '\n'
print "DEBUG: Number of squares for r_5\t {}\t\tmin_value: {}\t\tmax_value: {}".format(len(rd_5), min(rd_5), max(rd_5))
print '\tSides:\t', r_5_sides, '\n'


# assign constraint variables
problem.addVariable("r_0",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_4'} for i in rd_0])
problem.addVariable("r_1",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_4'} for i in rd_1])
problem.addVariable("r_2",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': 'r_3'} for i in rd_2])
problem.addVariable("r_3",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': ['r_2', 'r_4']} for i in rd_3])
problem.addVariable("r_4",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': ['r_0', 'r_1', 'r_3']} for i in rd_4])
problem.addVariable("r_5",
                    [{'sq': i['sq'], 'a': i['a'], 'b': i['b'], 'adjacent': ['r_4']} for i in rd_5])

# problem.addConstraint(lambda r_0, r_1, r_2, r_3, r_4:
#                       9 < sum([r_0['a'], r_1['a'], r_2['a'], r_3['a'], r_4['a']]) < 10,
#                       ['r_0', 'r_1', 'r_2', 'r_3', 'r_4'])

problem.addConstraint(lambda r_0, r_1, r_2, r_3, r_4, r_5:
                      30 < sum([r_0['sq'], r_1['sq'], r_2['sq'], r_3['sq'], r_4['sq'], r_5['sq']]) < 40,
                      ['r_0', 'r_1', 'r_2', 'r_3', 'r_4', 'r_5'])
start = time.time()
solutions = problem.getSolutions()
finish = time.time()

solutions_number = len(solutions)
print ' DEBUG: Number of Solutions\t{}\t\tTime for Searching\t{} seconds.\n'.format(solutions_number, finish - start)


import csv

with open('rooms_a_b.csv', 'w') as csvfile:
    fieldnames = ['r_0_a', 'r_0_b', 'r_1_a', 'r_1_b', 'r_2_a', 'r_2_b', 'r_3_a', 'r_3_b', 'r_4_a', 'r_4_b', 'r_5_a', 'r_5_b']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for sol in solutions:
        out = {}
        for k, v in sol.items():
            out["{}_a".format(k)] = v['a']
            out["{}_b".format(k)] = v['b']
        writer.writerow(out)
