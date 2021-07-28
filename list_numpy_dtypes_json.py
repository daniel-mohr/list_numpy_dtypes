#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-07-28
:License: BSD 3-Clause License
"""

import json
import numpy
import re
import sys


data = dict()
data['environment'] = {
    'sys.version': sys.version,
    'sys.api_version': sys.api_version,
    'sys.byteorder': sys.byteorder,
    'sys.copyright': sys.copyright,
    'sys.executable': sys.executable,
    'sys.float_info': sys.float_info,
    'sys.float_repr_style': sys.float_repr_style,
    'sys.implementation': sys.implementation.__dict__,
    'sys.int_info': sys.int_info,
    'sys.maxsize': sys.maxsize,
    'sys.platform': sys.platform,
    'numpy.version.full_version': numpy.version.full_version,
    'numpy.version.git_revision': numpy.version.git_revision}
data['dtypes'] = dict()
dtypes_data = data['dtypes']

for i in range(24):
    nat = numpy.array([], dtype=numpy.sctypeDict[i])
    dtypes_data[i] = dict()
    dtypes_data[i]['dtype'] = re.findall(r"'(.*)'", str(numpy.sctypeDict[i]))
    dtypes_data[i]['nat.dtype'] = str(nat.dtype)
    dtypes_data[i]['dtype.char'] = nat.dtype.char
    dtypes_data[i]['dtype.kind'] = nat.dtype.kind
    dtypes_data[i]['dtype.num'] = nat.dtype.num
    dtypes_data[i]['dtype.itemsize'] = nat.dtype.itemsize
    dtypes_data[i]['dtype.str'] = nat.dtype.str
    dtypes_data[i]['dtype.name'] = nat.dtype.name

with open('data.json', 'w') as fd:
    json.dump(data, fd)

print(json.dumps(data, indent=2))
