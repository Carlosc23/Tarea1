# Carlos Calderon , 15219
# Graphics
# Homework  1

# Define variables
from random import randint

import numpy as np

from SR1 import software_render

option = 0
x = software_render('image.bmp')


def menu():
    return '---¡Bienvenido a la tarea 1 de graficas por computadora!---\n\nPor favor con el teclado ingrese el número' \
           ' de acuerdo a la instrucción que desea ver, Una imagen con el resultado sera guardada en la ubicación ' \
           'de este proyecto \n\n' \
           '-----------------------------------------------------------------------------------------------------' \
           '-------------------------------\n' \
           '1. Por renderizar <una imagen negra con un punto blanco en una ubicación random dentro de la imagen.\n' \
           '2. Por renderizar una imagen negra con un punto blanco en cada esquina\n' \
           '3. Por renderizar un cubo de 100 pixeles en el centro de su imagen\n' \
           '4. Por renderizar líneas blancas en toda la orilla de su imagen (4 lineas) \n' \
           '5. Por renderizar una línea blanca en diagonal por el centro de su imagen. \n' \
           '6. Por llenar su imagen entera de puntos blancos y negros ' \
           '(las posibilidades de que un punto sea blanco o negro son de 50%)\n' \
           '7. Por llenar su imagen entera de puntos de colores random \n' \
           '8. Por crear una escena de un cielo con estrellas \n' \
           '9. Por crear una escena de 160 x 192 pixeles representando un frame de un juego de Atari.(Pong)\n' \
           '10. Para salir' \
           '-----------------------------------------------------------------------------------------------------' \
           '-------------------------------\n'


while option != 9:
    print(menu())
    option = input('Ingrese una opción')

    if option == '1':
        x.glCreateWindow(700, 700)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(200, 200, 200, 200)
        x.glColor(0, 255, 255)
        x.glVertex(randint(-1, 1), randint(-1, 1))
        x.glFinish()

    elif option == "2":
        x.glCreateWindow(700, 700)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(200, 200, 200, 200)
        x.glColor(255, 255, 255)
        x.glVertex(-1, 1)
        x.glVertex(-1, -1)
        x.glVertex(1, -1)
        x.glVertex(1, 1)
        x.glFinish()

    elif option == "3":
        x.glCreateWindow(700, 700)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 700, 700)
        x.glColor(255, 255, 255)
        x.square(100)
        x.glFinish()

    elif option == "4":
        x.glCreateWindow(400, 400)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 400, 400)
        x.glColor(255, 255, 255)
        x.drawLeftLine(10)
        x.drawTopLine(10)
        x.drawBottonLine(10)
        x.drawRightLine(10)
        x.glFinish()

    elif option == "5":
        x.glCreateWindow(400, 400)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 400, 400)
        x.glColor(255, 255, 255)
        x.diagonal()
        x.glFinish()

    elif option == "6":
        x.glCreateWindow(400, 400)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 400, 400)
        x.glColor(255, 255, 255)
        x.random_point()
        x.glFinish()

    elif option == "7":
        x.glCreateWindow(400, 400)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 400, 400)
        x.glColor(255, 255, 255)
        x.random_point_color()
        x.glFinish()

    elif option == "8":
        x.glCreateWindow(400, 400)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 395, 395)
        x.glColor(255, 255, 255)
        x.sky(100)
        x.glFinish()

    elif option == "9":
        x.glCreateWindow(160, 192)
        x.glClearColor(0, 0, 0)
        x.glClear()
        x.glViewPort(0, 0, 160, 192)
        x.glColor(255, 255, 255)

        x.glVertex(0, 1)
        x.glVertex(0, 0.9)
        #x.glVertex(0, 0.8)
        x.glVertex(0, 0.7)
        x.glVertex(0, 0.6)
        #x.glVertex(0, 0.5)

        x.glVertex(0, 0.4)
        x.glVertex(0, 0.3)
        # x.glVertex(0, 0.2)
        x.glVertex(0, 0.1)
        x.glVertex(0, 0)

        x.glVertex(0, -0.3)
        x.glVertex(0, -0.4)
        #x.glVertex(0, -0.5)
        x.glVertex(0, -0.6)
        x.glVertex(0, -0.7)
        #x.glVertex(0, -0.8)
        x.glVertex(0, -0.9)
        x.glVertex(0, -1)
        #x.glVertex(0, -1.1)
        #x.glVertex(0, -1.2)
        #x.glVertex(0, -1.3)
        #x.glVertex(0, -1.4)


        for i in np.arange(-.5, -0.2, 0.02):
            x.glVertex(-1, i,   5)
        # ----------
        for i in np.arange(0.3, 0.6, 0.02):
            x.glVertex(0.95, i,   5)
        """
        x.glVertex(1, 0)
        x.glVertex(1, 0.02)
        x.glVertex(1, 0.04)
        x.glVertex(1, 0.06)
        x.glVertex(1, 0.08)
        x.glVertex(1, 0.1)
        x.glVertex(1, 0.12)
        x.glVertex(1, 0.14)
        """
        # -------------
        x.glVertex(0.5, 0.5)
        # img.square(100)
        x.glFinish()
