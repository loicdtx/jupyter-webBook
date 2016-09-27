
# Perhaps jinja2 is a more lightweigth solution
from jinja2 import Template, Environment, FileSystemLoader
import nbformat
from nbconvert import HTMLExporter
import json
from os import makedirs
from os.path import exists, splitext
from jbook import jupyterChapter
from pprint import pprint

# Variables
dir_out = "_site"

# Get the list of files (and title of the book) from the file "_book.json"
with open("_book.json") as src:
    book_meta = json.load(src)

# Create _site directory
if not exists(dir_out):
    makedirs(dir_out)

chapters = []
# For each file:
for file in book_meta['chapters']['file_names']:
    chapter = jupyterChapter(file)
    chapter.readNotebook()
    chapter.getTitle()
    chapters.append(chapter)

chapter_list = []
for id, chapter in enumerate(chapters):
    nav_elements = dict()
    nav_elements['name'] = chapter.title
    href = splitext(book_meta['chapters']['file_names'][id])[0] + '.html'
    nav_elements['href'] = href
    nav_elements['class'] = 'none'
    chapter_list.append(nav_elements)

for chapter in chapters:
    chapter.addChapterList(chapter_list)
    env = Environment(loader = FileSystemLoader('templates'))
    template = env.get_template('default.html')
    html_out = template.render(chapters = chapter.chapter_list, notebook_content = chapter.notebook[0])
    with open(splitext(chapter.filename)[0] + '.html', 'wb') as dst:
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

