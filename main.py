#!/usr/bin/env python3

import markdown2
import os

dict_fname_title = dict()


def convert(name: str):
    if not os.path.exists('arts'):
        os.mkdir('arts')
    html = markdown2.markdown_path('raws/{}.md'.format(name),
                                   extras=['fenced-code-blocks', 'toc'])
    with open('arts/{}.html'.format(name), 'w') as f:
        f.writelines([html.toc_html, html])


def get_title(fullname: str) -> str:
    with open('raws/'+fullname, 'r') as f:
        return f.readline()[7:-9]


def get_raws():
    global dict_fname_title
    if not os.path.exists('raws'):
        os.mkdir('raws')
    raws = os.listdir('raws')
    for i in raws:
        dict_fname_title[os.path.splitext(i)[0]] = get_title(i)
    return


def update_index():
    ids = ['<title>风沐白的部落格 | entr0pia\'s blog</title>']
    for k, v in dict_fname_title.items():
        i = '{}【{}】'.format(k[:10], v)
        uri = 'arts/{}.html'.format(k)
        ids.append('[{}]({})'.format(i, uri))
    ids.sort(reverse=True)
    html = markdown2.markdown('\n\n'.join(ids))
    with open('index.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    get_raws()
    list(map(convert, list(dict_fname_title.keys())))
    update_index()
