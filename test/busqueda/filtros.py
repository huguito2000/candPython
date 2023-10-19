import random

from objetos.funciones import click_elemento, text_elemento, comboBox
from test.login import loginValido
from objetos.busqueda.obj_filtros import misVancates, filtros, buscar, puesto, ubicacion, cbUbicacion, salario, sMin, \
    sMax, jornada, cbJornada, modalidad, cbModalidad, contratacion, cbContratacion, tipoEmpresa, cbTipoEmpresa, fecha, \
    cbFecha, filtrarVacantes

carpeta = 'filtros'
loginValido()

click_elemento(misVancates,carpeta, 2)
click_elemento(filtros, carpeta, 2)
click_elemento(filtros, carpeta, 2)

puestos = ['abogado', 'desarrollador', 'medico', 'contador', 'Filósofo', 'Profesor', 'Periodista', 'Enfermero']
aleatorio = random.choice(puestos)

text_elemento(puesto,aleatorio, carpeta, 2)
click_elemento(filtrarVacantes, carpeta, 2)

click_elemento(ubicacion, carpeta, 2)
comboBox(cbUbicacion, 7, carpeta, 2)





