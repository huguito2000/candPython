import time
from datetime import datetime
from objetos.browser import driver
from objetos.registro.obj_registro import crearCuenta, email, siguiente, token
from objetos.funciones import text_elemento, click_elemento, captura_time

now = datetime.now()
correo = 'cand' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)

carpeta = 'registro'
def registroPruebas():
    try:
        click_elemento(crearCuenta, carpeta, 2)
        text_elemento(email, 'huguito.candidato', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        text_elemento(email, 'huguito.candidatoyopmail.com', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        text_elemento(email, 'huguito.candidato@yopmail', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        text_elemento(email, 'huguito.candidato@yopmail.com', carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        text_elemento(email, correo, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        captura_time(carpeta, 2)
        print('paso el registro')
        return 'paso el registro'
    except Exception as e:
        print('no paso el registro')
        return 'no paso el registro'
def registroValido():
    click_elemento(crearCuenta, carpeta, 2)
    text_elemento(email, correo, carpeta, 2)
    click_elemento(siguiente, carpeta, 2)
    time.sleep(2)
    driver.get(token)
    time.sleep(1)


