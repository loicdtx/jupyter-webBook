from jinja2 import Template, Environment, FileSystemLoader
import nbformat
from nbconvert import HTMLExporter
import json
from os import makedirs
from os.path import exists, basename
from jbook import jupyterChapter, copy_and_overwrite
from shutil import copytree
from copy import copy
from pprint import pprint

# Variables
dir_out = "_site"
chapters = []
nav_chapters = []

# Get the list of files (and title of the book) from the file "_book.json"
with open("_book.json") as src:
    book_meta = json.load(src)

# Create _site directory and add css to it
if not exists(dir_out):
    makedirs(dir_out)

copy_and_overwrite('static/css', "_site/css")

# Build jupyterChapter class for each file
# TODO: function buildClassList()
for file in book_meta['chapters']['file_names']:
    chapter = jupyterChapter(file)
    chapter.readNotebook()
    chapter.getTitle()
    chapter.makeFilenameOut()
    chapters.append(chapter)

# Build a list containing all chapters information to build the navbar
# TODO: function buildNavbarList()
for chapter in chapters:
    nav_elements = dict()
    nav_elements['name'] = chapter.title
    nav_elements['href'] = basename(chapter.filename_out)
    nav_elements['class'] = 'none'
    nav_chapters.append(nav_elements)

# Add navbar elements to each chapter, feed html template and write to file
for chapter in chapters:
    chapter.addChapterList(nav_chapters)
    chapter.activateNavClass()
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('default.html')
    html_out = template.render(chapters = chapter.chapter_list, notebook_content = chapter.notebook)
    with open(chapter.filename_out, 'w') as dst:
        dst.write(html_out)