import time

from objetos.browser import driver
from objetos.cv.obj_mis_datos import perfil
from test.login import loginValido
from objetos.funciones import click_elemento, scrollearElemento
from objetos.busqueda.obj_filtros import misVancates
from objetos.busqueda.obj_favoritos import busqueda, favoritos, corazon1, corazon2, corazon3, corazon4, favorito1, \
    favorito2, favorito3, favorito4, cerrarSesion

def seccionFavoritos():
    try:
        loginValido()
        carpeta = 'favoritos'

        click_elemento(misVancates, carpeta, 2)
        click_elemento(corazon1, carpeta, 2)
        click_elemento(corazon2, carpeta, 2)
        click_elemento(corazon3, carpeta, 2)
        click_elemento(corazon4, carpeta, 2)
        print('se selecciono los favoritos')
        time.sleep(2)

        click_elemento(favoritos, carpeta, 2)
        click_elemento(favorito4, carpeta, 2)
        click_elemento(favorito3, carpeta, 2)
        click_elemento(favorito2, carpeta, 2)
        click_elemento(favorito1, carpeta, 2)
        time.sleep(5)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)


        print('ya paso la seccion de favoritos')
        return 'ya paso la seccion de favoritos correctamente'
    except Exception as e:
        print('no paso la seccion de favoritos', str(e))
        return 'no ya paso la seccion de favoritos'


