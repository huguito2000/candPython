import time
from test.registro.telefono import telefono
from objetos.funciones import text_elemento, click_elemento, comboBox,pdf,nombres, apellidos, fechaNac
from objetos.registro.obj_informacion1 import subirCV, nombre1, nombre2, apellidoP, apellidoM, fecha, nacionalidad, \
    edoCivil, genero, siguiente, rutapdf

def informacion1():
    try:
        telefono()
        carpeta = 'informacion'
        pdf(subirCV,rutapdf, carpeta, 2)
        time.sleep(30)
        text_elemento(nombre1, '1234', carpeta, 2)
        text_elemento(nombre2, '56789', carpeta, 2)
        text_elemento(apellidoP, '1234', carpeta, 2)
        text_elemento(apellidoM, '56789', carpeta, 2)
        text_elemento(apellidoM, '12122000', carpeta, 2)
        text_elemento(fecha, '12122023', carpeta, 2)
        text_elemento(fecha, '12121800', carpeta, 2)
        nombres(nombre1, carpeta, 1)
        nombres(nombre2, carpeta, 1)
        apellidos(apellidoP, carpeta, 2)
        apellidos(apellidoM, carpeta, 2)
        fechaNac(fecha, carpeta, 2)
        comboBox(nacionalidad, 1, carpeta, 1)
        time.sleep(1)
        comboBox(edoCivil, 1, carpeta, 2)
        time.sleep(1)
        comboBox(genero, 2, carpeta, 2)
        time.sleep(1)
        click_elemento(siguiente, carpeta, 2)
        print('ya paso la información de los nombres')
        return 'ya paso la información de los nombres'
    except Exception as e:
        print('no paso la informacion', str(e))
        return 'no paso la informacion'

informacion1()