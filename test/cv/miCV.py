import time

from test.login import loginValido
from objetos.funciones import click_elemento, scrollearElemento
from objetos.cv.miCV.Obj_videoPresentacion import grabar, masTarde, continuar, pregunta1, pregunta2, pregunta3, \
    pregunta4, iniciarGrabacion, siguientePregunta, detener, reiniciar, guardar

loginValido()

carpeta = 'miCV'
scrollearElemento(grabar, carpeta, 2)
click_elemento(grabar, carpeta, 2)

click_elemento(continuar, carpeta, 1)
click_elemento(pregunta1, carpeta, 1)
click_elemento(pregunta2, carpeta, 1)
click_elemento(continuar, carpeta, 1)

click_elemento(iniciarGrabacion, carpeta, 2)
time.sleep(15)
click_elemento(siguientePregunta, carpeta, 2)
click_elemento(detener, carpeta, 2)
click_elemento(reiniciar, carpeta, 2)

click_elemento(iniciarGrabacion, carpeta, 2)
time.sleep(15)
click_elemento(siguientePregunta, carpeta, 2)
click_elemento(detener, carpeta, 2)
click_elemento(guardar, carpeta, 2)
time.sleep(5)

