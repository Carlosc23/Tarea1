import random
import struct
from math import ceil
from random import randint
import math


def char(c):
    return struct.pack("=c", c.encode('ascii'))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([b, g, r])


class Bitmap(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = []
        self.r = 0
        self.g = 0
        self.b = 0
        self.vpWidth = 0
        self.vpHeight = 0
        self.vpX = 0
        self.vpY = 0
        self.vr = 0
        self.vg = 0
        self.vb = 0
        self.clear()

    def clear(self):
        self.pixels = [
            [color(self.r, self.g, self.b) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glViewPort(self, x, y, width, height):
        if height <= 0 or width <= 0:
            print('Height and width must be positives')
            input()
        elif x < 0 or y < 0 or x > self.width or y > self.height:
            print('x and y must be positives and smaller tha height and width')
        else:
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x
            self.vpY = y

    def glClear(self):
        self.pixels = [
            [
                # show background color
                color(self.r, self.g, self.b) for x in range(self.width)
            ]
            for y in range(self.height)
        ]

    def glClearColor(self, r, g, b):
        self.r = ceil(r * 255)
        self.g = ceil(g * 255)
        self.b = ceil(b * 255)

    def glVertex(self, x, y,pointSize=10):

        if self.vpHeight != 0 or self.vpWidth != 0:
            xx = x * ((self.vpWidth - pointSize) / 2)
            yy = y * ((self.vpHeight - pointSize) / 2)
            localX = self.vpX + int((self.vpWidth - pointSize) / 2) + int(xx)
            localY = self.vpY + int((self.vpHeight - pointSize) / 2) + int(yy)
            print(x, y, localX, localY)
            for x in range(pointSize):
                for y in range(pointSize):
                    self.point(localX + x, localY + y)
        else:
            print('Debe de ejecutar glViewPort para obtener un área a gráficar')

    def glColor(self, r, g, b):
        self.vr = r
        self.vg = g
        self.vb = b

    def write(self, filename):
        f = open(filename, 'bw')

        # file header (14)
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header (40)
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.pixels[x][y])
        f.close()

    def point(self, x, y, color=color(255, 255, 255)):
        self.pixels[y][x] = color

    def square(self, size):
        cordX = int((self.vpWidth / 2)) - int(size / 2)
        cordY = int((self.vpWidth / 2)) - int(size / 2)
        for x in range(cordX, cordX + size):
            for y in range(cordY, cordY + size):
                self.point(x, y)

    # draw left line
    def drawLeftLine(self, padding):
        x = padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    # draw rigth line
    def drawRightLine(self, padding):
        x = self.vpWidth - padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    # draw top line
    def drawTopLine(self, padding):
        y = padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    # draw botton line
    def drawBottonLine(self, padding):
        y = self.vpHeight - padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def diagonal(self):
        for cord in range(self.vpX, self.vpWidth):
            self.point(cord, cord)

    def random_point(self):
        whiteColor = [255, 255, 255]
        blackColor = [0, 0, 0]
        for y in range(self.height):
            for x in range(self.width):
                self.glColor(*random.choice([whiteColor, blackColor]))
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def random_point_color(self):
        whiteColor = [255, 255, 255]
        blackColor = [0, 0, 0]
        for y in range(self.height):
            for x in range(self.width):
                self.glColor(randint(0, 255), randint(0, 255), randint(0, 255))
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def sky(self, stars):
        loop = 0
        while (loop < stars):
            loop = loop + 1
            size = randint(1, 3)
            x = randint(0, self.vpWidth - size - 2)
            y = randint(0, self.vpHeight - size - 2)
            self.printStar(x, y, size)

    def printStar(self, x, y, size):
        for cordX in range(size):
            for cordY in range(size):
                self.point(cordX + x, cordY + y)

# r = Bitmap(600, 400)
# r.write('out.bmp')
# r.point(100, 200, color(255, 255, 0))
