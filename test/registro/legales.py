from objetos.funciones import click_elemento, scrollearElemento
from test.registro.crearPass import crearPass
from objetos.registro.obj_legales import privacidad, aceptar, terminos, aceptar2, cookies, aceptar3, mejorarCV, \
    siguiente
carpeta = 'legales'
def legales():
    try:
        crearPass()
        click_elemento(privacidad, carpeta, 2)
        scrollearElemento(aceptar, carpeta, 2)
        click_elemento(aceptar, carpeta, 2)

        click_elemento(terminos, carpeta, 2)
        scrollearElemento(aceptar2, carpeta, 2)
        click_elemento(aceptar2, carpeta, 2)

        click_elemento(cookies, carpeta, 2)
        scrollearElemento(aceptar3, carpeta, 2)
        click_elemento(aceptar3, carpeta, 2)

        click_elemento(mejorarCV, carpeta, 2)

        click_elemento(siguiente, carpeta, 2)
        print('ya paso legales')
        return 'ya paso legales'
    except Exception as e:
        print('no paso legales', str(e))
        return 'no pase legales'

