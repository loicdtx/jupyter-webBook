from jinja2 import Template, Environment, PackageLoader
import json
from os import makedirs
from os.path import exists, basename, join, dirname
import os, sys
from jbook.chapter import jupyterChapter, copy_and_overwrite
import click


def buildChapterList(x, title, dir_out):
    chap = jupyterChapter(x, title)
    chap.readNotebook()
    chap.getTitle()
    chap.makeFilenameOut(dir_out)
    return chap

def makeNavBarList(x):
    nav_elements = dict()
    nav_elements['name'] = x.title
    nav_elements['href'] = basename(x.filename_out)
    nav_elements['class'] = 'none'
    return nav_elements


@click.command()
def nb2book():
    # Variables
    dir_out = '_site'

    # Get the list of files (and title of the book) from the file "_book.json"
    with open("_book.json") as src:
        book_meta = json.load(src)

    # Create _site directory and add css to it
    if not exists(dir_out):
        makedirs(dir_out)

    css_dir = join(dirname(sys.modules['jbook'].__file__), 'static/css')
    js_dir = join(dirname(sys.modules['jbook'].__file__), 'static/js')
    copy_and_overwrite(css_dir, join(dir_out, "css"))
    copy_and_overwrite(js_dir, join(dir_out, "js"))
    copy_and_overwrite(book_meta['assets'], join(dir_out, book_meta['assets']))

    #TODO: repeat for assets
    title = book_meta['title']

    # Build jupyterChapter class for each file and make a list of it
    chapters = [buildChapterList(x, title, dir_out) for x in book_meta['files']]

    # Build a list of navbar elements
    navbar_list = map(makeNavBarList, chapters)

    # Add navbar elements to each chapter, feed html template and write to file
    for chap in chapters:
        chap.addChapterList(navbar_list)
        chap.activateNavClass()
        chap.numberChapters()
        env = Environment(loader=PackageLoader('jbook', 'templates'))
        template = env.get_template('default.html')
        html_out = template.render(chapters = chap.chapter_list,\
                                   notebook_content = chap.notebook,\
                                   webbook_title = chap.webbook_title)
        with open(chap.filename_out, 'w') as dst:
            dst.write(html_out)
