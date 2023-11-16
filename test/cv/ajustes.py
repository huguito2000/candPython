import random
import time

from objetos.obj_login import cerrarSesion
from test.login import loginValido
from objetos.browser import driver
from objetos.cv.obj_mis_datos import perfil
from objetos.funciones import text_elemento, click_elemento, codigo, borrarTexto, scrollearElemento
from objetos.cv.ajustes.obj_cuentaSeguridad import ajustes, cuentaSeguridad, correo, email, passwordEmail, mostrarEmail, \
    ocultarEmail, siguienteEmail, telefono, phone, passwordPhone, mostrarPhone, ocultarPhone, siguientePhone, code, \
    code1, code2, code3, code4, volveEnviar, siguientePhone2, passw, password, mostrar1, ocultar1, passwordNew, \
    mostrar2, ocultar2, passwordNew2, mostrar3, ocultar3, cambiar
from objetos.cv.ajustes.obj_legales import legales, terminoCondiciones, aceptar, avisoPrivacidad, aceptar2, cookies, \
    aceptar3
from objetos.cv.ajustes.obj_eliminarCuenta import incidencia, eliminarCuenta, continuarEli, passEliminar, \
    mostrarEliminar, ocultarEliminar, eliminar, miCV
def Ajustes():
    try:
        loginValido()
        time.sleep(2)
        carpeta = 'ajustes'
        click_elemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(ajustes, carpeta, 2)
        click_elemento(cuentaSeguridad, carpeta, 2)

        click_elemento(telefono, carpeta, 2)
        click_elemento(passw, carpeta, 2)
        click_elemento(correo, carpeta, 2)

        text_elemento(email, 'huguito.candidato@yopmail.com', carpeta, 2)
        text_elemento(passwordEmail, 'Abcd.1234', carpeta, 2)
        click_elemento(siguienteEmail, carpeta, 2)

        numEmail = str(random.randint(0, 100))
        text_elemento(email, 'hugo' + numEmail + '@yopmail.com', carpeta, 2)
        text_elemento(passwordEmail, 'abcd.1234', carpeta, 2)
        click_elemento(mostrarEmail, carpeta, 2)
        text_elemento(passwordEmail, 'Abcd.1234', carpeta, 2)
        click_elemento(ocultarEmail, carpeta, 2)
        click_elemento(siguienteEmail, carpeta, 2)
        time.sleep(2)

        # telefono
        click_elemento(telefono, carpeta, 2)

        text_elemento(phone, '1111111111', carpeta, 2)
        text_elemento(passwordPhone, 'Abcd.1234', carpeta, 2)
        click_elemento(siguientePhone, carpeta, 2)

        text_elemento(phone, '5569777077', carpeta, 2)
        text_elemento(passwordPhone, 'abcd.1234', carpeta, 2)
        click_elemento(mostrarPhone, carpeta, 2)
        text_elemento(passwordPhone, 'Abcd.1234', carpeta, 2)
        click_elemento(ocultarPhone, carpeta, 2)
        click_elemento(siguientePhone, carpeta, 2)
        time.sleep(1)

        codigo(code, carpeta, code1, code2, code3, code4, 2)
        click_elemento(volveEnviar, carpeta, 2)
        click_elemento(siguientePhone2, carpeta, 2)
        codigo(code, carpeta, code1, code2, code3, code4, 2)
        click_elemento(siguientePhone2, carpeta, 2)
        time.sleep(5)

        # cambio de contraseña
        click_elemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(ajustes, carpeta, 2)

        click_elemento(cuentaSeguridad, carpeta, 2)
        click_elemento(passw, carpeta, 2)
        text_elemento(password, 'abcd.1234', carpeta, 2)
        click_elemento(mostrar1, carpeta, 2)
        text_elemento(passwordNew, 'Abcd.1234', carpeta, 2)
        text_elemento(passwordNew2, 'Abcd.1234', carpeta, 2)
        click_elemento(cambiar, carpeta, 2)

        borrarTexto(passwordNew2, 1)
        borrarTexto(passwordNew, 1)

        text_elemento(password, 'Abcd.1234', carpeta, 2)
        click_elemento(mostrar2, carpeta, 1)

        text_elemento(passwordNew, 'abcdefgh', carpeta, 2)
        text_elemento(passwordNew, 'ABCDEFGH', carpeta, 2)
        text_elemento(passwordNew, '12345678', carpeta, 2)
        text_elemento(passwordNew, 'Abcdefgh', carpeta, 2)
        text_elemento(passwordNew, 'Abcd123', carpeta, 2)
        text_elemento(passwordNew, 'Abcd.1234', carpeta, 2)

        click_elemento(mostrar3, carpeta, 1)
        text_elemento(passwordNew2, 'Abcd.12345', carpeta, 2)
        text_elemento(passwordNew2, 'Abcd.1234', carpeta, 2)
        click_elemento(ocultar1, carpeta, 1)
        click_elemento(ocultar2, carpeta, 1)
        click_elemento(ocultar3, carpeta, 1)
        click_elemento(cambiar, carpeta, 2)

        #legales
        loginValido()
        time.sleep(2)

        click_elemento(perfil, carpeta, 2)
        time.sleep(2)
        click_elemento(ajustes, carpeta, 2)
        click_elemento(legales, carpeta, 2)

        click_elemento(terminoCondiciones, carpeta, 2)
        scrollearElemento(aceptar, carpeta, 1)
        click_elemento(aceptar, carpeta, 1)

        click_elemento(avisoPrivacidad, carpeta, 1)
        scrollearElemento(aceptar2, carpeta, 1)
        click_elemento(aceptar2, carpeta, 1)

        click_elemento(cookies, carpeta, 1)
        scrollearElemento(aceptar3, carpeta, 1)
        click_elemento(aceptar3, carpeta, 1)

        #levantar inicdencia
        click_elemento(incidencia, carpeta, 2)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])

        # eliminar cuenta
        click_elemento(eliminarCuenta, carpeta, 2)
        click_elemento(continuarEli, carpeta, 2)
        click_elemento(eliminar, carpeta, 2)
        text_elemento(passEliminar, 'abcd.1234', carpeta, 2)
        click_elemento(mostrarEliminar, carpeta, 2)
        click_elemento(ocultarEliminar, carpeta, 2)
        click_elemento(eliminar, carpeta, 2)
        time.sleep(5)
        click_elemento(perfil, carpeta, 2)

        click_elemento(miCV, carpeta, 2)
        time.sleep(1)
        click_elemento(perfil, carpeta, 2)
        click_elemento(cerrarSesion, carpeta, 2)

        print('ya paso ajustes')
        return 'ya paso la seccion de ajustes correctamente'
    except Exception as e:
        print('no paso ajustes', str(e))
        return 'no paso ajustes'

Ajustes()