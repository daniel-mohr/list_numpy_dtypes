#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-07-22
:License: BSD 3-Clause License
"""

import numpy
import sys

def print_header():
    print('|            dtype             | dtype.char | dtype.kind | dtype.num | a.dtype.str |')
    print('|------------------------------|------------|------------|-----------|-------------|')

def print_data_type_line(a):
    print('| {:<28} |     {:>2}     |    {:>2}      |    {:>2}     |    {:>4}     |'.format(
        str(numpy.sctypeDict[i]), a.dtype.char, a.dtype.kind, a.dtype.num,
        a.dtype.str))

print('environment:')
print(sys.version)
print()
print(
    '[numpy.dtype](https://numpy.org/devdocs/reference/arrays.dtypes.html):\n')

print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    print_data_type_line(a)

print('only integers:\n')
print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    if a.dtype.kind == 'i':
        print_data_type_line(a)

print('only floats:\n')
print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    if a.dtype.kind == 'f':
        print_data_type_line(a)
