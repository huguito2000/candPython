import time

from objetos.cv.miCV.Obj_certificaciones import agregar, certificado, institucion, fecha, si, no, IDCertificacion, UrlCertificado, regresar, guardar
from objetos.funciones import click_elemento, text_elemento
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido

def certificacion():
    try:
        carpeta = 'certificacion'
        loginValido()
        time.sleep(1)
        click_elemento(agregar, carpeta, 1)
        click_elemento(regresar, carpeta, 1)
        click_elemento(agregar, carpeta, 1)
        text_elemento(certificado, 'istbq', carpeta, 1)
        text_elemento(institucion, 'udemy', carpeta, 1)
        text_elemento(fecha, '12122000', carpeta, 1)
        click_elemento(si, carpeta, 1)
        click_elemento(no, carpeta, 1)
        text_elemento(IDCertificacion, '123456certificado', carpeta, 1)
        text_elemento(UrlCertificado, 'wwww.google.com', carpeta, 1)
        click_elemento(guardar, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se agrego la certificacion')
        return 'se agreggo la certificacion'
    except Exception as e:
        print('No se agrego la certificado')
        return 'No se agrego la certificado'