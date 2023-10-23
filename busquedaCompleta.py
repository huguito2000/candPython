from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from test.busqueda.favoritos import seccionFavoritos
from test.busqueda.filtros import filtrosBusqueda
from test.busqueda.postulacion import postulacionCorrecta



now = datetime.now()
fecha = str(now.day) + ' del ' + str(now.month) + " en el minuto " + str(now.minute)

def generar_informe_pdf(nombre_archivo, reporte_Favoritos, reporte_Filtros, reporte_Postulacion):
    global fecha
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.drawString(72, 750, "Informe de busqueda completa")
    c.drawString(72, 720, "Fecha: " + fecha + " del 2023")

    # Agregar detalles sobre la ejecución
    c.drawString(72, 690, "Resultado de la pruebas en las funciones de la sección de busqueda y postulacion")
    c.drawString(72, 670, reporte_Favoritos)
    c.drawString(72, 640, reporte_Filtros)
    c.drawString(72, 610, reporte_Postulacion)
    c.save()

def busquedaPostulacion():
    resultado_Favoritos = seccionFavoritos()
    resultado_Filtros = filtrosBusqueda()
    resultado_Postulacion = postulacionCorrecta()

    nombre_archivo = "reportes/cvCompleto " + fecha + ".pdf"
    generar_informe_pdf(nombre_archivo, resultado_Favoritos, resultado_Filtros, resultado_Postulacion)

