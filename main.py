#!/usr/bin/env python3

import markdown2
import os

dict_fname_title = dict()

forms = ['<meta charset="UTF-8">\n',
         '<link rel="icon" type="image/x-icon" href="/imgs/favicon.ico">\n',
         '<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/markdown-css-smartisan/github-markdown.css"/>\n',
         '<link rel="stylesheet" type="text/css" href="/codehilite.css"/>\n',
         '<style>\n',
         '.toc {\n',
         '  width: 20%;\n',
         '  float: left;\n',
         '  position: fixed;\n',
         '  top: 2%;\n',
         '}\n',
         '.markdown-body {\n',
         '  width: 60%;\n',
         '  margin-right: 10%;\n',
         '  float: right;\n',
         '}\n',
         '</style>\n']


def convert(name: str):
    if not os.path.exists('arts'):
        os.mkdir('arts')
    html = markdown2.markdown_path('raws/{}.md'.format(name),
                                   extras=['fenced-code-blocks', 'toc'])
    with open('arts/{}.html'.format(name), 'w') as f:
        f.writelines([*forms,
                      '<div class="toc">\n', html.toc_html, '</div>\n',
                      '<div class="markdown-body">\n', html, '</div>\n'])


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
    ids = []
    for k, v in dict_fname_title.items():
        i = '{}【{}】'.format(k[:10], v)
        uri = 'arts/{}.html'.format(k)
        ids.append('[{}]({})'.format(i, uri))
    ids.sort(reverse=True)
    html = markdown2.markdown('\n\n'.join(ids))
    with open('index.html', 'w') as f:
        f.writelines(['<title>风沐白的部落格 | entr0pia\'s blog</title>\n',
                      '<meta charset="UTF-8">\n',
                      '<link rel="icon" type="image/x-icon" href="/imgs/favicon.ico">\n',
                      '<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/markdown-css-smartisan/github-markdown.css"/>\n',
                      '<style>\n',
                      '.markdown-body {\n',
                      '  width: 80%;\n',
                      '  margin: auto;\n',
                      '}\n',
                      '</style>\n'
                      '<div class="markdown-body">\n', html, '</div>\n'])


if __name__ == '__main__':
    get_raws()
    list(map(convert, list(dict_fname_title.keys())))
    update_index()
