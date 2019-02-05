import struct
from random import randint, random

from math import ceil
from Bitmap import *


class software_render(object):
    def __init__(self, filename):
        self.window = ""
        self.filename = filename
        self.glInit()

    def glInit(self):
        pass

    def glCreateWindow(self, width, height):
        self.window = Bitmap(width, height)

    def glViewPort(self, x, y, width, height):
        self.window.glViewPort(x, y, width, height)

    def glClear(self):
        self.window.clear()

    def glClearColor(self, r, g, b):
        self.window.glClearColor(r, g, b)

    def glVertex(self, x, y):
        self.window.glVertex(x, y)

    def glColor(self, r, g, b):
        self.window.glColor(r, g, b)

    def glFinish(self):
        self.window.write(self.filename)

    def square(self, size):
        self.window.square(size)

    # draw left line
    def drawLeftLine(self, padding):
        self.window.drawLeftLine(padding)

    # draw rigth line
    def drawRightLine(self, padding):
        self.window.drawRightLine(padding)

    # draw top line
    def drawTopLine(self, padding):
        self.window.drawTopLine(padding)

    # draw botton line
    def drawBottonLine(self, padding):
        self.window.drawBottonLine(padding)

    def diagonal(self):
        self.window.diagonal()

    def random_point(self):
        self.window.random_point()

    def random_point_color(self):
        self.window.random_point_color()
