#!/usr/bin/python

__author__ = 'as1986'


def retrieve_file(partial_url):
    import requests
    from bs4 import BeautifulSoup

    r = requests.get('http://mojim.com{}'.format(partial_url))
    soup = BeautifulSoup(r.text)
    ly = soup.select("#fsZ")
    if len(ly) == 0:
        return None
    raw = [x for x in ly[0].stripped_strings]
    return raw


def main():
    import sys
    import json

    for idx, l in enumerate(open(sys.argv[1])):
        (title, js) = l.strip().split('\t')
        lyrics_list = json.loads(js)
        print 'title: {}, js: {}\n'.format(title, lyrics_list)
        retrieved_lyrics = []
        for lyrics in lyrics_list:
            retrieved_lyrics.append(retrieve_file(lyrics))
        with open('{}.lyrics'.format(idx), 'w') as w_fh:
            w_fh.write('{}\t{}\n'.format(title, json.dumps(retrieved_lyrics)))

    return


if __name__ == '__main__':
    main()