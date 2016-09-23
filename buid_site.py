#!/usr/bin/env python

# Perhaps jinja2 is a more lightweigth solution
from jinja2 import Template
import json
from os import makedirs
from os.path import exists
from pprint import pprint

# Variables
dir_out = "_site"

# Get the list of files (and title of the book) from the file "_book.json"
with open("_book.json") as src:
    book_meta = json.load(src)

# Create _site directory
if not exists(dir_out):
    makedirs(dir_out)

pprint(book_meta)
# For each file:
    # Open and read it
    # Generate html string
    # Retrieve h1 and h2s (store the list of h1 and h2s for later)
    # Generate file and add html string to it


# For each html file generated
    # Read the file
    # Fill the navbar

