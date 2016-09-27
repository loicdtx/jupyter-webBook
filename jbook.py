import nbformat
from nbconvert import HTMLExporter
from bs4 import BeautifulSoup

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
        self.notebook = html_exporter.from_notebook_node(chapter_nb)

    def getTitle(self):
        soup = BeautifulSoup(self.notebook[0], 'html.parser')
        self.title = soup.h1.contents[0]
    def addChapterList(self, chapter_list):
        self.chapter_list = chapter_list




