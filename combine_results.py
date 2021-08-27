#!/usr/bin/python3
"""
:Author: Daniel Mohr
:Email: daniel.mohr@dlr.de
:Date: 2021-08-27
:License: BSD 3-Clause License
"""

import datetime
import html
import json
import re


def read_json(filename):
    with open(filename, 'r') as fd:
        json_instance = json.load(fd)
    return json_instance


def numpydtypelink(content):
    link = '<a href="https://numpy.org/doc/stable/reference/' \
        'arrays.scalars.html#%s" target="_blank">%s</a>' % (
            content, html.escape(content[6:]))
    return link


def sysversion(source):
    return html.escape(source["environment"]["sys.version"])


def sysbyteorder(source):
    return html.escape(source["environment"]["sys.byteorder"])


def numpyversion(source):
    return html.escape(source["environment"]["numpy.version.full_version"])

def intcell(content):
    return '<td align="center">%i</td>' % content

def strcell(content):
    return '<td align="center">%s</td>' % html.escape(content)

names = ['Linux (x86_64)',
         'i386/ubuntu:18.04 (Linux (x86))',
         'i386/debian:latest (Linux (x86))',
         'macOS',
         'Windows']
data = dict()
data[names[0]] = dict()
data[names[0]]['names'] = ['Ubuntu 18.04 LTS', 'Ubuntu 20.04 LTS']
data[names[0]]['json'] = [read_json('ubuntu-1804_listing/data.json'),
                          read_json('ubuntu-2004_listing/data.json')]
data[names[0]]['link'] = [
    'https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu1804-README.md',
    'https://github.com/actions/virtual-environments/blob/main/images/linux/Ubuntu1804-README.md']
data[names[1]] = dict()
data[names[1]]['names'] = ['i386/ubuntu:18.04']
data[names[1]]['json'] = [read_json('ubuntu-1804_i386_listing/data.json')]
data[names[1]]['link'] = ['https://hub.docker.com/r/i386/ubuntu']
data[names[2]] = dict()
data[names[2]]['names'] = ['i386/debian:latest']
data[names[2]]['json'] = [read_json('debian_i386_listing/data.json')]
data[names[2]]['link'] = ['https://hub.docker.com/r/i386/debian/']
data[names[3]] = dict()
data[names[3]]['names'] = ['macOS 10.15']
data[names[3]]['json'] = [read_json('macos-1015_listing/data.json')]
data[names[3]]['link'] = ['https://github.com/actions/virtual-environments/blob/main/images/macos/macos-10.15-Readme.md']
data[names[4]] = dict()
data[names[4]]['names'] = ['Microsoft Windows Server 2016 Datacenter',
                           'Microsoft Windows Server 2019 Datacenter']
data[names[4]]['json'] = [read_json('windows-2016_listing/data.json'),
                          read_json('windows-2019_listing/data.json')]
data[names[4]]['link'] = [
    'https://github.com/actions/virtual-environments/blob/main/images/win/Windows2016-Readme.md',
    'https://github.com/actions/virtual-environments/blob/main/images/win/Windows2019-Readme.md']

bgcolor1 = ["#DDDDDD", "#FFFFFF"]
bgcolor2 = ["#BBBBDD", "#DDDDFF"]

with open('index.html', 'w') as fd:
    fd.write('<html>\n')
    fd.write('<head>\n')
    fd.write(
        '<meta name="date" content="%s">\n' % datetime.date.today().isoformat())
    fd.write('<meta name="DC.Date" content="%s">\n' %
             datetime.date.today().isoformat())
    fd.write('</head>\n')
    fd.write('<body>\n')
    fd.write('<h1 align="center">listing of '
             '<a href="https://numpy.org/" target="_blank">numpy</a> '
             'dtypes</h1>\n')
    fd.write('<p>This table is generate by '
             '<a href="https://github.com/daniel-mohr/list_numpy_dtypes" '
             'target="_blank">list_numpy_dtypes</a> on %s:</p>\n' %
             datetime.date.today().isoformat())
    # generate table
    fd.write('<p><table border="1" rules="all">\n')
    # head lines
    fd.write('<tr align="center">')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/'
             'generated/numpy.dtype.num.html" target="_blank">'
             'dtype.num</a></th>')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/'
             'generated/numpy.dtype.char.html" target="_blank">'
             'dtype.char</a></th>')
    fd.write('<th rowspan="2"><a href="https://numpy.org/devdocs/reference/'
             'generated/numpy.dtype.kind.html" target="_blank">'
             'dtype.kind</a></th>')
    for name in names:
        fd.write('<th colspan="3">%s</th>' % html.escape(name))
    fd.write('</tr>\n')
    fd.write('<tr align="center">')
    for name in names:
        fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/'
                 'numpy.dtype.html" target="_blank">dtype</a></th>')
        fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/'
                 'numpy.dtype.str.html" target="_blank">dtype.str</a></th>')
        fd.write('<th><a href="https://numpy.org/devdocs/reference/generated/'
                 'numpy.dtype.itemsize.html" target="_blank">'
                 'dtype.itemsize</a></th>')
    # body lines
    for i in range(24):
        fd.write('<tr bgcolor="%s">' % bgcolor1[0])
        fd.write(intcell(i))
        for attr in ['dtype.char', 'dtype.kind']:
            for j in range(len(names)):
                for k in range(len(data[names[j]]['json'])):
                    assert(data[names[0]]['json'][0]['dtypes'][str(i)][attr] ==
                           data[names[j]]['json'][k]['dtypes'][str(i)][attr])
            fd.write(strcell(data[names[0]]['json'][0]['dtypes'][str(i)][attr]))
        for name in names:
            if name == names[0]:
                act = data[name]['json'][0]['dtypes'][str(i)]
                # dtype
                res = re.findall(r"'(.*)'", act['dtype'][0])
                if not bool(res):
                    res = re.findall(r"(.*)", act['dtype'][0])
                res = res[0]
                fd.write('<td align="center">%s</td>' % numpydtypelink(res))
                # dtype.str
                fd.write(strcell(act['dtype.str']))
                # dtype.itemsize
                fd.write(intcell(act['dtype.itemsize']))
            else:
                ref = data[names[0]]['json'][0]['dtypes'][str(i)]
                act = data[name]['json'][0]['dtypes'][str(i)]
                if ((ref['dtype'][0] == act['dtype'][0]) and
                    (ref['dtype.str'] == act['dtype.str']) and
                    (ref['dtype.itemsize'] == act['dtype.itemsize'])):
                    fd.write(
                        '<td align="center" colspan="3" bgcolor="%s">'
                        'same as Linux (x86_64)</td>' % bgcolor2[0])
                else:
                    # dtype
                    res = re.findall(r"'(.*)'", act['dtype'][0])
                    if not bool(res):
                        res = re.findall(r"(.*)", act['dtype'][0])
                    res = res[0]
                    fd.write('<td align="center">%s</td>' % numpydtypelink(res))
                    # dtype.str
                    fd.write(strcell(act['dtype.str']))
                    # dtype.itemsize
                    fd.write(intcell(act['dtype.itemsize']))
        fd.write('</tr>\n')
        bgcolor = bgcolor1[0]
        bgcolor1[0] = bgcolor1[1]
        bgcolor1[1] = bgcolor
        bgcolor = bgcolor2[0]
        bgcolor2[0] = bgcolor2[1]
        bgcolor2[1] = bgcolor
    # foot
    fd.write('</table></p>')
    # description
    for name in names:
        fd.write('<p>The %s results were generated on:\n' % name)
        fd.write('<ul>\n')
        for i in range(len(data[name]['names'])):
            fd.write(' <li><a href="%s">%s</a>\n' % (data[name]['link'][i],
                                                     data[name]['names'][i]))
            fd.write('  <ul>\n')
            fd.write('   <li>sys.version: %s</li>\n' %
                     sysversion(data[name]['json'][i]))
            fd.write('   <li>sys.byteorder: %s</li>\n' %
                     sysbyteorder(data[name]['json'][i]))
            fd.write('   <li>numpy.version.full_version: %s</li>\n' %
                     numpyversion(data[name]['json'][i]))
            fd.write('  </ul>\n')
            fd.write(' </li>\n')
        fd.write('</ul></p>\n')
    # html end
    fd.write('</body>\n')
    fd.write('</html>\n')
