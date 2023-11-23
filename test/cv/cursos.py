from objetos.cv.miCV.Obj_curso import agregar, curso, institucion, fecha, horas, cancelar, guardar
from objetos.funciones import click_elemento, text_elemento
from objetos.cv.obj_mis_datos import perfil
from objetos.obj_login import cerrarSesion
from test.login import loginValido

def cursos():
    try:
        carpeta = 'cursos'
        loginValido()
        click_elemento(agregar, cancelar, 1)
        click_elemento(cancelar, carpeta, 1)
        click_elemento(agregar, cancelar, 1)
        text_elemento(curso, 'istqb', carpeta, 1)
        text_elemento(institucion, 'udemy', carpeta, 1)
        text_elemento(fecha, '12122000', carpeta, 1)
        text_elemento(horas, '12', carpeta, 1)
        click_elemento(guardar, carpeta, 1)

        click_elemento(perfil, carpeta, 1)
        click_elemento(cerrarSesion, carpeta, 1)
        print('se agrego el curso')
        return 'se agrego el curso'
    except Exception as e:
        print('se agrego el curso', str(e))
        return 'Se agrego el curso'

