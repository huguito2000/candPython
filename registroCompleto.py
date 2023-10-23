from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.registro import registro1, crearPass2, legales3, telefono4, informacion5, informacion6
now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month)+ " en el minuto " +str(now.minute)

def generar_informe_pdf(nombre_archivo, reporteRegistro, reporteCrearPass, reporteLegales, reporteTelefono, reporteInformacion, reporteInformacion2):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de registro completo")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de registro completo")
    c.drawString(72, 670, reporteRegistro),
    c.drawString(72, 640, reporteCrearPass)
    c.drawString(72, 610, reporteLegales)
    c.drawString(72, 580, reporteTelefono)
    c.drawString(72, 550, reporteInformacion)
    c.drawString(72, 520, reporteInformacion2)

    c.save()


def registroTest():
    resultado_registro = registro1.registroPruebas()
    resultado_CrearPass = crearPass2.passPruebas()
    resultado_legales = legales3.legales()
    resultado_Telefono = telefono4.telefono()
    resultado_Infomracion1 = informacion5.informacion1()
    resultado_Infomracion2 = informacion6.registroCompleto()
    nombre_archivo = "reportes/registro " + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_registro, resultado_CrearPass, resultado_legales, resultado_Telefono, resultado_Infomracion1, resultado_Infomracion2)
