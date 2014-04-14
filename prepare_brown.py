#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'as1986'


def main():
    import json, sys,cleaner, glob


    with open('brown_output', 'w') as w_fh:
        lyrics_files = glob.glob('*.lyrics')
        for each_lyr in lyrics_files:
            for each_l in open(each_lyr):
                (title, js) = each_l.strip().split('\t')
                list_lyrics = json.loads(js)
                if list_lyrics is not None and len(list_lyrics) > 0:
                    lyr = cleaner.clean(list_lyrics[0])
                    for each_lyrline in lyr:
                        to_append = ' '.join(each_lyrline.strip()).encode('utf-8'
                                                                          '')
                        w_fh.write(to_append + '\n')

    return


if __name__ == '__main__':
    main()