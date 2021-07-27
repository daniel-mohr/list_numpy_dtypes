#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-07-27
:License: BSD 3-Clause License
"""

import json


def read_json(filename):
    with open(filename, 'r') as fd:
        json_instance = json.load(fd)
    return json_instance


ubuntu_1804_listing = read_json('ubuntu-1804_listing/data.json')
ubuntu_2004_listing = read_json('ubuntu-2004_listing/data.json')
macos_1015_listing = read_json('macos-1015_listing/data.json')
windows_2016_listing = read_json('windows-2016_listing/data.json')
windows_2019_listing = read_json('windows-2019_listing/data.json')
print(type(macos_1015_listing))


table = []
for i in range(24):
    line = [i]  # dtype.num
    for attr in ['dtype.char', 'dtype.kind',
                 'dtype.str', 'dtype.num', 'dtype.itemsize']:
        line.append(ubuntu_1804_listing['dtypes'][str(i)][attr])  # dtype.kind
        for data in [ubuntu_2004_listing, macos_1015_listing,
                     windows_2016_listing, windows_2019_listing]:
            assert(ubuntu_1804_listing['dtypes'][str(i)][attr] ==
                   data['dtypes'][str(i)][attr])
    for data in [ubuntu_1804_listing, ubuntu_2004_listing, macos_1015_listing,
                 windows_2016_listing, windows_2019_listing]:
        line.append(data['dtypes'][str(i)]['dtype'])  # dtype
    table.append(line)
print(table)
