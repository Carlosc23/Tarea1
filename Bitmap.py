# Carlos Calderon, 15219
# Bitmap.py
# Inspired in the class render made in Graphics Course C3044
import random
import struct
import sys

from math import ceil


def char(c):
    return struct.pack("=c", c.encode('ascii'))


def word(w):
    return struct.pack("=h", w)


def dword(d):
    return struct.pack("=l", d)


def color(r, g, b):
    return bytes([b, g, r])


class Bitmap(object):
    """
    Class that abstract a bitmap
    """

    def __init__(self, width, height):
        """
        Constructor that initialize necessary variables for
        render images
        :param width: width of the image that will be render
        :param height: height of the image that will be render
        """
        self.width = width
        self.height = height
        self.pixels = []
        self.r = 255
        self.g = 0
        self.b = 0
        self.pointSize = 5
        self.vr = 255
        self.vg = 200
        self.vb = 200
        self.glclear()

    def glclear(self):
        """
        Fill the the pixels object with a color
        :return:
        """
        self.pixels = [
            [color(self.r, self.g, self.b) for x in range(self.width)]
            for y in range(self.height)
        ]

    def glViewPort(self, x, y, width, height):
        """
        Define the area of the image where the glVertex will draw
        :param x: number that represent the horizontal coord where the viewport will be drawn
        :param y: number that represent the vertical coord where the viewport will be drawn
        :param width: width of the viewport
        :param height: heigth of the viewport
        :return:
        """
        if height <= 0 or width <= 0:
            print('Height and width must be positives')
        elif x < 0 or y < 0 or x > self.width or y > self.height:
            print('x and y must be positives and smaller tha height and width')
        else:
            self.vpWidth = width
            self.vpHeight = height
            self.vpX = x
            self.vpY = y

    def glClearColor(self, r, g, b):
        """
        change the default colors that uses glClear to fill
        :param r: amount of red
        :param g: amount of green
        :param b: amount of blue
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.r = ceil(r * 255)
            self.g = ceil(g * 255)
            self.b = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def glVertex(self, x, y):
        """
        Change the color of a point of the screen, relative to ViewPort
        :param x: relative horizontal coord of the point
        :param y: relative vertical coord of the point
        :return:
        """

        if self.vpHeight != 0 and self.vpWidth != 0:
            xx = x * ((self.vpWidth - self.pointSize) / 2)
            yy = y * ((self.vpHeight - self.pointSize) / 2)
            localX = self.vpX + int((self.vpWidth - self.pointSize) / 2) + int(xx)
            localY = self.vpY + int((self.vpHeight - self.pointSize) / 2) + int(yy)
            print(x, y, localX, localY)
            for x in range(self.pointSize):
                for y in range(self.pointSize):
                    self.point(localX + x, localY + y, color(self.vr, self.vb, self.vg))
        else:
            print('Initialize glViewPort')
            sys.exit()

    def set_point_size(self, pointSize):
        """
        change the size of the global point, default is 5
        :param pointSize: size of the class point
        :return:
        """
        self.pointSize = pointSize

    def glColor(self, r, g, b):
        """
        Change the color of glVertex
        :param r: amount of red
        :param g: amount of green
        :param b: amount of b
        :return:
        """
        if 0 <= r <= 1 or 0 <= g <= 1 or 0 <= b <= 1:
            self.vr = ceil(r * 255)
            self.vg = ceil(g * 255)
            self.vb = ceil(b * 255)
        else:
            print("Please insert numbers between 0 and 1")
            sys.exit()

    def write(self, filename):
        """
        Save the image in a file
        :param filename: name of the file that will be saved
        :return:
        """
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

    def point(self, x, y, color=color(255, 200, 200)):
        """
        function that fills a pixel of a color
        :param x: position of the pixel
        :param y: position of the pixel
        :param color: color that will fill the pixel
        :return:
        """
        self.pixels[y][x] = color

    def square(self, size):
        cordx = int((self.vpWidth / 2)) - int(size / 2)
        cordy = int((self.vpWidth / 2)) - int(size / 2)
        for x in range(cordx, cordx + size):
            for y in range(cordy, cordy + size):
                self.point(x, y)

    def drawLeftLine(self, padding):
        x = padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawRightLine(self, padding):
        x = self.vpWidth - padding
        for y in range(padding, self.vpHeight - padding):
            self.point(x, y)

    def drawTopLine(self, padding):
        y = padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def drawBottomLine(self, padding):
        y = self.vpHeight - padding
        for x in range(padding, self.vpWidth - padding):
            self.point(x, y)

    def diagonal(self):
        for cord in range(self.vpX, self.vpWidth):
            self.point(cord, cord)

    def random_point(self):
        whiteColor = [1, 1, 1]
        blackColor = [0, 0, 0]
        for y in range(self.height):
            for x in range(self.width):
                self.glColor(*random.choice([whiteColor, blackColor]))
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def random_point_color(self):

        for y in range(self.height):
            for x in range(self.width):
                list_random = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                list_random_norm = [float(i) / 255 for i in list_random]
                self.glColor(list_random_norm[0], list_random_norm[1], list_random_norm[2])
                self.point(x, y, color(self.vr, self.vg, self.vb))

    def sky(self, stars):
        counter = 0
        while counter < stars:
            counter += 1
            size = random.randint(1, 3)
            x = random.randint(0, self.vpWidth - size - 2)
            y = random.randint(0, self.vpHeight - size - 2)
            self.printStar(x, y, size)

    def printStar(self, x, y, size):
        for cordX in range(size):
            for cordY in range(size):
                self.point(cordX + x, cordY + y)
# r = Bitmap(600, 400)
# r.write('out.bmp')
# r.point(100, 200, color(255, 255, 0))
