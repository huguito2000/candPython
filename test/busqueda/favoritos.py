from objetos.browser import driver
from test.login import loginValido
from objetos.funciones import click_elemento
from objetos.busqueda.obj_filtros import misVancates
from objetos.busqueda.obj_favoritos import busqueda, favoritos, corazon1, corazon2, corazon3, corazon4, favorito1, \
    favorito2, favorito3, favorito4

def favoritos():
    try:
        loginValido()
        carpeta = 'favoritos'

        click_elemento(misVancates, carpeta, 2)
        click_elemento(corazon1, carpeta, 2)
        click_elemento(corazon2, carpeta, 2)
        click_elemento(corazon3, carpeta, 2)
        click_elemento(corazon4, carpeta, 2)

        click_elemento(favoritos, carpeta, 2)
        click_elemento(favorito4, carpeta, 2)
        click_elemento(favorito3, carpeta, 2)
        click_elemento(favorito2, carpeta, 2)

        driver.quit()
        print('ya paso la seccion de favoritos')
        return 'ya paso la seccion de favoritos'
    except Exception as e:
        print('no paso la seccion de favoritos', str(e))
        return 'no ya paso la seccion de favoritos'


