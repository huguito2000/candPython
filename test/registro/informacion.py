import random
import time
from test.registro.telefono import telefono
from objetos.funciones import text_elemento, click_elemento, comboBox,pdf,nombres, apellidos, fechaNac
from objetos.registro.obj_informacion1 import subirCV, nombre1, nombre2, apellidoP, apellidoM, fecha, nacionalidad, \
    edoCivil, genero, siguiente

telefono()
carpeta = 'informacion'
time.sleep(3)
pdfs = ['alberto', 'carlos', 'cristian', 'daniel', 'diana', 'mario', 'octavio', 'romero']
aleatorio = random.choice(pdfs)
print(aleatorio)
rutapdf = '/Users/huguito/PycharmProjects/pythonProject/pythonProject/candidato/archivos/pdf/' + aleatorio + '.pdf'
print(rutapdf)

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
