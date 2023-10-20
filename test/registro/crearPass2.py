import time

from objetos.funciones import text_elemento, click_elemento, captura_time
from test.registro.registro1 import registroValido, registroPruebas
from objetos.registro.obj_crearPass import password, mostrar, ocultar, password2, mostrar2, ocultar2, siguiente

carpeta = 'crearPass'
def passPruebas ():
    try:
        registroPruebas()
        print('empieza la creacion de la password')
        time.sleep(2)
        text_elemento(password, 'abcd', carpeta, 2)
        click_elemento(mostrar, carpeta, 2)
        click_elemento(ocultar, carpeta, 2)

        text_elemento(password, '1234', carpeta, 2)
        click_elemento(mostrar, carpeta, 2)
        click_elemento(ocultar, carpeta, 2)

        text_elemento(password, 'ABCD', carpeta, 2)
        click_elemento(mostrar, carpeta, 2)
        click_elemento(ocultar, carpeta, 2)

        text_elemento(password, 'Abc123', carpeta, 2)
        click_elemento(mostrar, carpeta, 2)
        click_elemento(ocultar, carpeta, 2)

        text_elemento(password, 'Abcd.1234', carpeta, 2)
        click_elemento(mostrar, carpeta, 2)
        click_elemento(ocultar, carpeta, 2)

        text_elemento(password2, 'Abcd.12345', carpeta, 2)
        click_elemento(mostrar2, carpeta, 2)
        click_elemento(ocultar2, carpeta, 2)

        text_elemento(password2, 'Abcd.1234', carpeta, 2)
        click_elemento(mostrar2, carpeta, 2)
        click_elemento(ocultar2, carpeta, 2)

        click_elemento(siguiente, carpeta, 2)
        captura_time(carpeta, 2)

        print('se creo la pass')
        return  ' se creo la pass'
    except Exception as e:
        print('no se creo la pass', str(e))
        return 'no se creo la pass'

def crearPass():
    registroValido()
    text_elemento(password, 'Abcd.1234', carpeta, 2)
    click_elemento(mostrar, carpeta, 2)
    click_elemento(ocultar, carpeta, 2)

    text_elemento(password2, 'Abcd.1234', carpeta, 2)
    click_elemento(mostrar2, carpeta, 2)
    click_elemento(ocultar2, carpeta, 2)

    click_elemento(siguiente, carpeta, 2)
    captura_time(carpeta, 2)


