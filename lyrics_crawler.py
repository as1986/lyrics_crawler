#!/usr/bin/python

__author__ = 'as1986'


def get_url(song_title):
    from bs4 import BeautifulSoup
    import requests

    to_return = []

    r = requests.get('http://mojim.com/{}.html?t3'.format(song_title))
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('a'):
        if 'twy' in link.get('href'):
            to_return.append(link.get('href'))
    return to_return


def main():
    import sys, json

    with open('urls', 'w') as w_fh:
        for each_line in open(sys.argv[1]):
            w_fh.write('{}\t{}\n'.format(each_line.strip(), json.dumps(get_url(each_line.strip()))))
    return


if __name__ == '__main__':
    main()