#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pathlib
import string
import sys

import requests
from bs4 import BeautifulSoup


def get_language(url: str) -> str:
    def unknown_language():
        raise Exception('Unknown Language')

    return {
        'php':          lambda: 'php',
        'python':       lambda: 'python',
        'javascript':   lambda: 'javascript',
        'coffeescript': lambda: 'coffeescript',

    }.get(url.split('/')[-1], unknown_language)()


def transform_title2name(title: str) -> str:
    result = title.replace('Train: ', '', 1)
    result = result[::-1].replace(' | Codewars'[::-1], '', 1)[::-1]
    result = ''.join(
        x.lower() if x.lower() in string.ascii_letters + string.digits else ' '
        for x in result) \
        .replace('  ', ' ') \
        .replace('  ', ' ') \
        .replace(' ', '_') \
        .replace('__', '_')
    result = result[:-1] if result[-1] == '_' else result
    return result


def language2file_ext(s: str) -> str:
    def unknown_language():
        raise Exception('Unknown Language')

    return {
        'php':          lambda: '.php',
        'python':       lambda: '.py',
        'javascript':   lambda: '.js',
        'coffeescript': lambda: '.coffee',

    }.get(s, unknown_language)()


def language2comment_delimiter(language: str) -> str:
    def unknown_language():
        raise Exception('Unknown Language')

    return {
        'php':          lambda: '//',
        'python':       lambda: '#',
        'javascript':   lambda: '//',
        'coffeescript': lambda: '#',

    }.get(language, unknown_language)()


def main():
    url: str = ''.join(sys.argv[1:])
    assert len(url) != 0, f'"url={url}"'

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.find('title')

    language = get_language(url)
    name = transform_title2name(title.string)
    file_ext = language2file_ext(language)

    kyu_outer = soup.find('div', {'class': 'inner-small-hex is-extra-wide'})
    kyu = kyu_outer.span.string[0]

    print(
        json.dumps(
            {
                'language': language,
                'name':     name,
                'file_ext': file_ext,
                'kyu':      kyu,
            },
            indent=2,
            sort_keys=True,
            ensure_ascii=False
        )
    )

    path = pathlib.Path.cwd() / f'{language}' / f'kyu_{kyu}'
    path.mkdir(exist_ok=True, parents=True)
    filename = path / f'{name}{file_ext}'
    if filename.exists():
        raise FileExistsError(filename)
    filename.touch()
    with open(f'{filename}', mode='a', encoding='utf-8') as fh_out:
        fh_out.write(f'{language2comment_delimiter(language)} {url}\n')


if __name__ == '__main__':
    main()
