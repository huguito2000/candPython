import time

from objetos.funciones import text_elemento, click_elemento, captura_time, codigo
from test.registro.legales3 import legales
from objetos.registro.obj_telefono import campoTelefono, siguiente, cambioTelefono, volverEnviar, code, code1, code2, code3, \
    code4, siguiente2

def telefono():
    try:
        legales()
        carpeta = 'telefono'
        text_elemento(campoTelefono, '5569777077', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        print('se mando el nuevo codigo')
        click_elemento(cambioTelefono, carpeta, 2)
        text_elemento(campoTelefono, '5569777077', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)
        click_elemento(volverEnviar, carpeta, 2)

        codigo(code, carpeta, code1, code2, code3, code4, 2)
        click_elemento(siguiente2, carpeta, 2)

        print('ya paso el telefono')
        return 'ya paso el telefono'
    except Exception as e:
        print('no paso el telefono')
        return 'no paso el telefono'


