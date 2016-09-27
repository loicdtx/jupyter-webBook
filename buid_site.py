
# Perhaps jinja2 is a more lightweigth solution
from jinja2 import Template
import nbformat
from nbconvert import HTMLExporter
import json
from os import makedirs
from os.path import exists
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

titles = []
for chapter in chapters:
    titles.append(chapter.title)

for chapter in chapters:
    chapter.addChapterList(titles)


    

    # Open and read it
    # Generate html string
    # Retrieve h1 and h2s (store the list of h1 and h2s for later)
# jake_notebook = nbformat.reads(response, as_version=4)
# jake_notebook.cells[0]
    # Generate file and add html string to it


# For each html file generated
    # Read the file
    # Fill the navbar

