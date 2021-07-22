#!/usr/bin/python3

import numpy

def print_header():
    print('[numpy.dtype](https://numpy.org/devdocs/reference/arrays.dtypes.html):')
    print()
    print('|            dtype             | dtype.char | dtype.kind | dtype.num | a.dtype.str |')
    print('|------------------------------|------------|------------|-----------|-------------|')

def print_data_type_line(a):
    print('| {:<28} |     {:>2}     |    {:>2}      |    {:>2}     |    {:>4}     |'.format(
        str(numpy.sctypeDict[i]), a.dtype.char, a.dtype.kind, a.dtype.num,
        a.dtype.str))

print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    print_data_type_line(a)

print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    if a.dtype.kind == 'i':
        print_data_type_line(a)

print_header()
for i in range(24):
    a = numpy.array([], dtype=numpy.sctypeDict[i])
    if a.dtype.kind == 'f':
        print_data_type_line(a)
