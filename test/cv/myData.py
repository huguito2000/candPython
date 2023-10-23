import random
import time
from objetos.obj_login import cerrarSesion
from objetos.funciones import click_elemento, scrollearElemento, nombres, apellidos, text_elemento, fechaNac, comboBox, \
    borrarTexto, cambio_imagen
from test.login import loginValido
from objetos.cv.obj_mis_datos import perfil, misDatos, cancelar, nombre, apellidoP, apellidoM, fecha, genero, edoCivil, \
    nacionalidad, zonaActual, municipioA, sueldo, zonaTrabajo, municipioT, residenciaSi, residenciaNo, github, behance, \
    linkedIn, sitioPersonal, guardar, imgPerfil, img_path, continuarImg


def myDatos():
    try:
        loginValido()
        time.sleep(3)
        carpeta = 'mis datos'

        cambio_imagen(imgPerfil, img_path, carpeta, 2)
        click_elemento(continuarImg, carpeta, 2)
        time.sleep(5)

        click_elemento(perfil, carpeta, 2)
        click_elemento(misDatos, carpeta, 2)
        scrollearElemento(cancelar, carpeta, 2)
        time.sleep(3)
        click_elemento(cancelar, carpeta, 2)

        click_elemento(perfil, carpeta, 2)
        click_elemento(misDatos, carpeta, 2)

        nombres(nombre, carpeta, 2)
        apellidos(apellidoP, carpeta, 2)
        apellidos(apellidoM, carpeta, 2)
        text_elemento(fecha, '12122023', carpeta, 2)
        text_elemento(fecha, '12121888', carpeta, 2)
        fechaNac(fecha, carpeta, 2)

        comboBox(genero, 1, carpeta, 2)
        comboBox(genero, 2, carpeta, 2)
        comboBox(genero, 3, carpeta, 2)
        comboBox(genero, 4, carpeta, 2)
        comboBox(genero, 2, carpeta, 2)

        comboBox(edoCivil, 1, carpeta, 2)
        comboBox(edoCivil, 2, carpeta, 2)
        comboBox(edoCivil, 3, carpeta, 2)
        comboBox(edoCivil, 1, carpeta, 2)

        comboBox(nacionalidad, 2, carpeta, 2)
        comboBox(nacionalidad, 1, carpeta, 2)
        scrollearElemento(nacionalidad, carpeta, 2)

        comboBox(zonaActual, 11, carpeta, 2)
        comboBox(zonaActual, 7, carpeta, 2)

        comboBox(municipioA, 15, carpeta, 2)
        comboBox(municipioA, 10, carpeta, 2)

        scrollearElemento(sueldo, carpeta, 2)
        borrarTexto(sueldo, 1)
        candSueldo = random.randint(1000, 30000)
        text_elemento(sueldo, candSueldo, carpeta, 2)

        comboBox(zonaTrabajo, 11, carpeta, 2)
        comboBox(zonaTrabajo, 7, carpeta, 2)

        comboBox(municipioT, 15, carpeta, 2)
        comboBox(municipioT, 10, carpeta, 2)
        click_elemento(residenciaSi, carpeta, 2)
        click_elemento(residenciaNo, carpeta, 2)
        click_elemento(residenciaSi, carpeta, 2)
        text_elemento(github, 'https://github.com', carpeta, 2)
        text_elemento(behance, 'https://github.com', carpeta, 2)
        text_elemento(linkedIn, 'https://github.com', carpeta, 2)
        text_elemento(sitioPersonal, 'https://github.com', carpeta, 2)
        click_elemento(guardar, carpeta, 2)
        time.sleep(2)

        scrollearElemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)


        print('paso mis datos')
        return 'Paso la seccion de mis datos correctamente.'
    except Exception as e:
        print('no paso mis datos', str(e))
        return 'no paso la seccion de mis datos'

