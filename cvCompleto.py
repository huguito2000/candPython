from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.cv.myData import myDatos
from test.cv.ajustes import Ajustes
from test.cv.videoPresentacion import miCv


now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)

def generar_informe_pdf(nombre_archivo, reporte_misDatos, reporte_Ajustes, reporte_MyCv):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de cvCompleto completo")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de la sección de CV")
    c.drawString(72, 670, reporte_misDatos)
    c.drawString(72, 640, reporte_Ajustes)
    c.drawString(72, 610, reporte_MyCv)
    c.save()

def cvTest():
    resultado_misDatos = myDatos()
    resultado_Ajustes = Ajustes()
    resultado_MyCV = miCv()

    nombre_archivo = "reportes/cvCompleto " + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_misDatos, resultado_Ajustes, resultado_MyCV)

