import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
import os
from os.path import splitext, join
import shutil
import copy
import sys

sys.setrecursionlimit(10000)

class jupyterChapter(object):
    """docstring for jupyterChapter"""
    def __init__(self, filename, webbook_title = 'Jupyter WebBook'):
        self.filename = filename
        self.webbook_title = webbook_title
        self.title = "Missing chapter title"
        self.notebook = None

    def readNotebook(self):
        with open(self.filename) as src:
            chapter_raw = src.read().decode()
        chapter_nb = nbformat.reads(chapter_raw, as_version=4)
        html_exporter = HTMLExporter()
        html_exporter.template_file = 'basic'
        self.notebook = html_exporter.from_notebook_node(chapter_nb)[0]

    def getTitle(self):
        soup = BeautifulSoup(self.notebook, 'html.parser')
        self.title = soup.h1.contents[0]

    def addChapterList(self, chapter_list):
        self.chapter_list = copy.deepcopy(chapter_list)

    def makeFilenameOut(self, prefix):
        self.filename_out = join(prefix, splitext(self.filename)[0] + '.html')

    def activateNavClass(self):
        for item in self.chapter_list:
            if item['name'] == self.title:
                item['class'] = 'active'

    def numberChapters(self):
        for i, item in enumerate(self.chapter_list):
            item['name'] = str(i + 1) + '. ' + item['name']
        

        





def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
