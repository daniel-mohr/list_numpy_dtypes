#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-07-28
:License: BSD 3-Clause License
"""

import datetime
import html
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


table = []
# dtype.num
# dtype.char
# dtype.kind
# dtype
# dtype.str
# dtype.itemsize
for i in range(24):
    line = [str(i)]  # dtype.num
    for data in [ubuntu_1804_listing, ubuntu_2004_listing, macos_1015_listing,
                 windows_2016_listing, windows_2019_listing]:
        # check: dtype.num is always the same
        assert(data['dtypes'][str(i)]['dtype.num'] == i)
    for attr in ['dtype.char', 'dtype.kind']:
        line.append(ubuntu_1804_listing['dtypes'][str(i)][attr])
        for data in [ubuntu_2004_listing, macos_1015_listing,
                     windows_2016_listing, windows_2019_listing]:
            # check: dtype.char and dtype.kind are always the same
            assert(ubuntu_1804_listing['dtypes'][str(i)][attr] ==
                   data['dtypes'][str(i)][attr])
    # we expect ubuntu-1804, ubuntu-2004 and macos-1015 and
    # windows-2016, windows-2019 have the same behavior
    # check: ubuntu-1804, ubuntu-2004
    for data in [ubuntu_2004_listing]:
        for attr in ['dtype', 'dtype.str', 'dtype.itemsize']:
            assert(ubuntu_1804_listing['dtypes'][str(i)][attr] ==
                   data['dtypes'][str(i)][attr])
    # check: windows-2016, windows-2019
    for data in [windows_2019_listing]:
        for attr in ['dtype', 'dtype.str', 'dtype.itemsize']:
            assert(windows_2016_listing['dtypes'][str(i)][attr] ==
                   data['dtypes'][str(i)][attr])
    for data in [ubuntu_1804_listing, macos_1015_listing, windows_2019_listing]:
        for attr in ['dtype', 'dtype.str', 'dtype.itemsize']:
            line.append(str(data['dtypes'][str(i)][attr]))
    table.append(line)

with open('index.html', 'w') as fd:
    fd.write('<html>\n')
    fd.write('<head>\n')
    fd.write(
        '<meta name="date" content="%s">\n' % datetime.date.today().isoformat())
    fd.write('<meta name="DC.Date" content="%s">\n' %
             datetime.date.today().isoformat())
    fd.write('</head>\n')
    fd.write('<body>\n')
    fd.write('<h1 align="center">listing of <a href="https://numpy.org/" target="_blank">numpy</a> dtypes</h1>\n')
    fd.write('<p>This table is generate by: <a href="https://github.com/daniel-mohr/list_numpy_dtypes" target="_blank">list_numpy_dtypes</a></p>\n')
    fd.write('<p><table border="1" rules="all">\n')
    fd.write('<tr align="center">')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.num.html" target="_blank">dtype.num</a></th>')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.char.html" target="_blank">dtype.char</a></th>')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.kind.html" target="_blank">dtype.kind</a></th>')
    fd.write('<th colspan="3">Linux</th>')
    fd.write('<th colspan="3">macOS</th>')
    fd.write('<th colspan="3">Windows</th>')
    fd.write('</tr>\n')
    fd.write('<tr align="center">')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.html" target="_blank">dtype</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.str.html" target="_blank">dtype.str</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.itemsize.html" target="_blank">dtype.itemsize</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.html" target="_blank">dtype</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.str.html" target="_blank">dtype.str</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.itemsize.html" target="_blank">dtype.itemsize</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.html" target="_blank">dtype</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.str.html" target="_blank">dtype.str</a></th>')
    fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/numpy.dtype.itemsize.html" target="_blank">dtype.itemsize</a></th>')
    fd.write('</tr>\n')
    bgcolor1 = ["#DDDDDD", "#FFFFFF"]
    bgcolor2 = ["#BBBBDD", "#DDDDFF"]
    for line in table:
        fd.write('<tr bgcolor="%s">' % bgcolor1[0])
        for i in range(3):
            fd.write('<td align="center">%s</td>' % html.escape(line[i]))
        for i in range(3, 6):
            fd.write('<td align="center">%s</td>' % html.escape(line[i]))
        if ((line[3] == line[6]) and (line[4] == line[7]) and
                (line[5] == line[8]) and (line[3] == line[9]) and
                (line[4] == line[10]) and (line[5] == line[11])):
            fd.write(
                '<td align="center" colspan="3" bgcolor="%s">same as Linux</td>' % bgcolor2[0])
            fd.write(
                '<td align="center" colspan="3" bgcolor="%s">same as Linux</td>' % bgcolor2[0])
        else:
            for i in range(6, 9):
                fd.write('<td align="center">%s</td>' % html.escape(line[i]))
            for i in range(9, 12):
                fd.write('<td align="center">%s</td>' % html.escape(line[i]))
        fd.write('</tr>\n')
        bgcolor = bgcolor1[0]
        bgcolor1[0] = bgcolor1[1]
        bgcolor1[1] = bgcolor
        bgcolor = bgcolor2[0]
        bgcolor2[0] = bgcolor2[1]
        bgcolor2[1] = bgcolor
    fd.write('</table></p>')
    fd.write('<p>The Linux results were generated on:\n')
    fd.write('<ul>\n')
    fd.write(' <li><a href="https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu1804-README.md">Ubuntu 18.04.5 LTS</a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write(' <li><a href="https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu2004-README.md">Ubuntu 20.04.2 LTS</a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write('</ul></p>\n')
    fd.write('<p>The macOS results were generated on:\n')
    fd.write('<ul>\n')
    fd.write(' <li><a href="https://github.com/actions/virtual-environments/blob/main/images/macos/macos-10.15-Readme.md">macOS 10.15</a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write('</ul></p>\n')
    fd.write('<p>The Windows results were generated on:\n')
    fd.write('<ul>\n')
    fd.write(' <li><a href=""></a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write(' <li><a href="https://github.com/actions/virtual-environments/blob/main/images/win/Windows2016-Readme.md">Microsoft Windows Server 2016 Datacenter</a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write(' <li><a href="https://github.com/actions/virtual-environments/blob/main/images/win/Windows2019-Readme.md">Microsoft Windows Server 2019 Datacenter</a>\n')
    fd.write('  <ul>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('   <li></li>\n')
    fd.write('  </ul>\n')
    fd.write(' </li>\n')
    fd.write('</ul></p>\n')
    fd.write('</body>\n')
    fd.write('</html>\n')
