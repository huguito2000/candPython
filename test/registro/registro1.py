import time
from datetime import datetime
from objetos.registro.obj_registro import crearCuenta, email, siguiente, tokens, cBoxlegal1, cBoxlegal2, legales1, legales2
from objetos.funciones import text_elemento, click_elemento, captura_time, token
from objetos.browser import driver
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

        click_elemento(legales1, carpeta, 2)
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        click_elemento(legales2, carpeta, 2)
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        click_elemento(cBoxlegal1, carpeta, 2)
        click_elemento(cBoxlegal2, carpeta, 2)

        text_elemento(email, correo, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)

        captura_time(carpeta, 2)

        token(tokens)
        time.sleep(2)
        print('paso el registro')
        return 'paso el registro'
    except Exception as e:
        print('no paso el registro')
        return 'no paso el registro'


def registroValido():
    try:
        click_elemento(crearCuenta, carpeta, 2)
        text_elemento(email, correo, carpeta, 2)
        click_elemento(cBoxlegal1, carpeta, 2)
        click_elemento(cBoxlegal2, carpeta, 2)
        click_elemento(siguiente, carpeta, 2)
        time.sleep(2)
        token(tokens)
        print('paso el registro')
        return 'paso el registro'
    except Exception as e:
        print('no paso el registro')
        return 'no paso el registro'

