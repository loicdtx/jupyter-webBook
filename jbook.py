import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup
import os
from os.path import splitext
import shutil
import copy
import sys

sys.setrecursionlimit(10000)

class jupyterChapter(object):
    """docstring for jupyterChapter"""
    def __init__(self, filename):
        self.filename = filename
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

    def makeFilenameOut(self, prefix = '_site/'):
        self.filename_out = prefix + splitext(self.filename)[0] + '.html'

    def activateNavClass(self):
        for item in self.chapter_list:
            if item['name'] == self.title:
                item['class'] = 'active'

    def numberChapters(self):
        pass
        

        





def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)
