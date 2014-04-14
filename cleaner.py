#!/usr/bin/python
from __future__ import unicode_literals

__author__ = 'as1986'


def clean(list_of_lines):
    to_return = []
    for each_line in list_of_lines:
        if each_line.startswith('['):
            continue
        if '歌詞' in each_line:
            continue
        if '演唱' in each_line:
            continue
        if '作曲' in each_line:
            continue
        if '作詞' in each_line:
            continue
        if '編曲' in each_line:
            continue
        to_return.append(each_line)
    return to_return