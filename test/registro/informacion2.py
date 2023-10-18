import random

from test.registro.informacion import informacion1
from objetos.funciones import comboBox, click_elemento, text_elemento
from objetos.registro.obj_informacion2 import primerEmpleo, trabajo, zonaTrabajo, municipioT, zonaActual, municipioA, \
    sueldo, siguiente

def registroCompleto():
    try:
        puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
        aleatorio = random.choice(puestos)

        carpeta = 'informacion2'
        informacion1()

        comboBox(primerEmpleo, 1, carpeta,1)

        text_elemento(trabajo,aleatorio, carpeta, 2)

        comboBox(zonaTrabajo, 7, carpeta, 2)
        comboBox(municipioT, 10, carpeta, 2)

        comboBox(zonaActual, 7, carpeta, 2)
        comboBox(municipioA, 10, carpeta, 2)

        text_elemento(sueldo, 25000, carpeta, 2)

        click_elemento(siguiente, carpeta, 2)
        print('paso la informacion 2')
        return 'se completo el registro completo'
    except Exception as e:
        print('no paso la informacion 2', str(e))
        return 'no se completo el registro completo'



