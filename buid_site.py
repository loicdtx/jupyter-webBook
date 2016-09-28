from jinja2 import Template, Environment, FileSystemLoader
import nbformat
from nbconvert import HTMLExporter
import json
from os import makedirs
from os.path import exists, splitext
from jbook import jupyterChapter, copy_and_overwrite
from shutil import copytree
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
    chapters.append(chapter)

# Iterate throught the 
# TODO: function buildNavbarList
for chapter in chapters:
    nav_elements = dict()
    nav_elements['name'] = chapter.title
    href = splitext(chapter.filename)[0] + '.html'
    nav_elements['href'] = href
    nav_elements['class'] = 'none'
    nav_chapters.append(nav_elements)

for chapter in chapters:
    chapter.addChapterList(nav_chapters)
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('default.html')
    html_out = template.render(chapters = chapter.chapter_list, notebook_content = chapter.notebook)
    with open("_site/" + splitext(chapter.filename)[0] + '.html', 'wb') as dst:
        dst.write(html_out)




    # Open and read it
    # Generate html string
    # Retrieve h1 and h2s (store the list of h1 and h2s for later)
# jake_notebook = nbformat.reads(response, as_version=4)
# jake_notebook.cells[0]
    # Generate file and add html string to it


# For each html file generated
    # Read the file
    # Fill the navbar

