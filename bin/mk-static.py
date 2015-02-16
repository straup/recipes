#!/usr/bin/env python

import sys
import codecs
import os.path
import logging
import markdown

def write_header(fh, title=""):

    fh.write("""<!DOCTYPE html>
<html><head>
<title>%s</title>
<style type="text/css">
body { font-family:sans-serif; font-size: 1em; margin:2em; line-height: 1.3em; }
h1 { line-height: 1.5em !important; background-color: #ededed; padding:.2em; padding-left:0 !important; }
blockquote { font-style: italic !important; margin:0px !important; }
</style>
<meta name="apple-mobile-web-app-capable" content="yes" />
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<meta name="HandheldFriendly" content="true" />
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>""" % title)

def write_footer(fh):
    fh.write("""</body></html>""")

def mk_html(src, dest):

    fname = os.path.basename(src)
    title = fname.replace(".md", "")

    fh = codecs.open(dest, mode="w", encoding="utf-8")

    write_header(fh, title)

    fh.write(md2html(src))

    write_footer(fh)
    fh.close()

def md2html(path):

    fh = codecs.open(path, mode="r", encoding="utf-8")
    md = fh.read()
    return markdown.markdown(md)

    
if __name__ == '__main__':

    whoami = sys.argv[0]
    whoami = os.path.abspath(whoami)

    bin = os.path.dirname(whoami)
    root = os.path.dirname(bin)

    recipes = os.path.join(root, 'recipes')
    static = os.path.join(root, 'static')

    filelist = {}

    for root, dirs, files in os.walk(recipes):

        for f in files:

            if not f.endswith(".md"):
                continue

            if f == 'example.md':
                continue

            if f == 'README.md':
                continue

            fname = f.replace(".md", ".html")
            parent = root.replace(recipes, static)

            src = os.path.join(root, f)
            dest = os.path.join(parent, fname)

            if not os.path.isdir(parent):
                os.makedirs(parent)

            if not filelist.get(parent, None):
                filelist[parent] = []

            filelist[parent].append(dest)
            mk_html(src, dest)

    pages = []

    main = os.path.join(static, "index.html")
    mfh = codecs.open(main, mode="w", encoding="utf-8")
    write_header(mfh)
    
    for path, recipes in filelist.items():

        sect = os.path.basename(path)
        idx = os.path.join(path, "index.html")

        mfh.write("<li><a href=\"%s\">%s</a></li>" % (sect, sect))

        fh = codecs.open(idx, mode="w", encoding="utf-8")
        write_header(fh)

        fh.write("<h1>%s</h1>" % sect)
        fh.write("<ul>")

        for r in recipes:

            fname = os.path.basename(r)
            title = fname.replace(".html", "")
            title = title.replace("-", " ")
            title = title.replace("_", " ")
            
            fh.write("<li><a href=\"%s\">%s</a></li>" % (fname, title))

        fh.write("</ul>")
        write_footer(fh)
        fh.close()

    write_footer(mfh)
    mfh.close()

    print filelist
    sys.exit()
