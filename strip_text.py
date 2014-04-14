#!/usr/bin/python

__author__ = 'as1986'


def retrieve_file(partial_url):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('http://mojim.com/{}'.format(partial_url))
    soup = BeautifulSoup(r.text)
    raw = [x for x in soup.select("#fsZ")[0].stripped_strings]
    return raw


def main():
    import sys
    import json

    for l in open(sys.argv[1]):
        (title, js) = l.strip().split('\t')
        print 'title: {}, js: {}\n'.format(title, json.loads(js))

    return


if __name__ == '__main__':
    main()