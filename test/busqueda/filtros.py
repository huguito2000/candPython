import random
import time

from objetos.cv.obj_mis_datos import perfil
from test.login import loginValido
from objetos.funciones import click_elemento, text_elemento, comboBox, borrarTexto, scrollearElemento
from objetos.busqueda.obj_filtros import misVancates, filtros, buscar, puesto, ubicacion, cbUbicacion, salario, sMin, \
    sMax, jornada, cbJornada, modalidad, cbModalidad, contratacion, cbContratacion, tipoEmpresa, cbTipoEmpresa, fecha, \
    cbFecha, filtrarVacantes, cerrarSesion

def filtrosBusqueda():
    try:
        carpeta = 'filtros'

        loginValido()
        click_elemento(misVancates,carpeta, 2)
        click_elemento(filtros, carpeta, 2)
        click_elemento(filtros, carpeta, 2)
        min = random.randint(1000, 5000)
        max = random.randint(5000, 15000)

        puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
        aleatorio = random.choice(puestos)

        text_elemento(puesto,aleatorio, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(ubicacion, carpeta, 2)
        comboBox(cbUbicacion, 7, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(salario, carpeta, 2)
        text_elemento(sMin, min, carpeta, 2)
        text_elemento(sMax, max, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(jornada, carpeta, 2)
        comboBox(cbJornada, 1, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(modalidad, carpeta, 2)
        comboBox(cbModalidad, 1, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(contratacion, carpeta, 2)
        comboBox(cbContratacion, 1, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(tipoEmpresa, carpeta, 2)
        comboBox(cbTipoEmpresa, 1, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(fecha, carpeta, 2)
        comboBox(cbFecha, 1, carpeta, 2)
        click_elemento(filtrarVacantes, carpeta, 2)

        click_elemento(buscar, carpeta, 2)
        borrarTexto(puesto, 2)
        time.sleep(1)
        click_elemento(filtrarVacantes, carpeta, 2)
        time.sleep(2)

        scrollearElemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)

        print('ya paso el filtro de busqueda')
        return 'ya paso el filtro de busqueda'
    except Exception as e:
        print('no paso el filtro', str(e))
        return 'no paso el filtro'