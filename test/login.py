import time

from objetos.browser import driver
from objetos.obj_login import email, siguiente, password, mostrar, ocultar
from objetos.funciones import text_elemento, captura_time, click_elemento

carpeta = 'login'

def loginPruebas():
    try:
        click_elemento(siguiente, carpeta, 1)
        time.sleep(2)

        text_elemento(email, 'huguito.candidato', carpeta, 2)
        click_elemento(siguiente, carpeta, 1)

        text_elemento(email, 'huguito.candidato@yopmail', carpeta, 2)
        click_elemento(siguiente, carpeta, 1)

        text_elemento(email, 'huguito.candidato@yopmail.com', carpeta, 2)
        click_elemento(siguiente, carpeta, 1)

        text_elemento(password, 'abcd.1234', carpeta, 2)
        click_elemento(mostrar, carpeta, 1)
        click_elemento(ocultar, carpeta, 1)
        click_elemento(mostrar, carpeta, 1)
        time.sleep(2)
        click_elemento(siguiente, carpeta, 1)
        time.sleep(1)
        print('manda llamar login valido')
        loginValido()

        print('se hizo login')
        return 'se hizo login pruebas'
    except Exception  as e:
        print('no se hizo login', str(e))
        return 'no se hizo login pruebas'


def loginValido():
    try:
        text_elemento(email, 'huguito.candidato@yopmail.com', carpeta, 2)
        text_elemento(password, 'Abcd.1234', carpeta, 1)
        click_elemento(siguiente, carpeta, 3)
        print('se hizo login')
        return 'se hizo login correctamente'
    except Exception as e:
        print('no se hizo login valido', str(e))
        return 'no se hizo login valido'


#cand18103552@yopmail.com