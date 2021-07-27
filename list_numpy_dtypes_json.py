#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-07-27
:License: BSD 3-Clause License
"""

import json
import numpy
import sys


data = dict()
data['environment']: {'sys.version': sys.version,
                      'numpy.version.full_version': numpy.version.full_version,
                      'numpy.version.git_revision': numpy.version.git_revision}
data['dtypes'] = dict()
dtypes_data = data['dtypes']

for i in range(24):
    nat = numpy.array([], dtype=numpy.sctypeDict[i])
    dtypes_data[i] = dict()
    # dtypes_data[i]['dtype'] = str(numpy.sctypeDict[i])
    dtypes_data[i]['dtype'] = str(nat.dtype)
    dtypes_data[i]['dtype.char'] = nat.dtype.char
    dtypes_data[i]['dtype.kind'] = nat.dtype.kind
    dtypes_data[i]['dtype.num'] = nat.dtype.num
    dtypes_data[i]['dtype.itemsize'] = nat.dtype.itemsize
    dtypes_data[i]['dtype.str'] = nat.dtype.str

with open('data.json', 'w') as fd:
    json.dump(data, fd)
