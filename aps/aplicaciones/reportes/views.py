from django.shortcuts import render
from django.views.generic import TemplateView
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.solicitudCambio.models import solicitudCambio, votos
from django.http import HttpResponse
from aps.settings import MEDIA_ROOT, IMAGENES_ROOT
# Create your views here.

class reporteProyecto(TemplateView):
    template_name = 'reportes/proyecto.html'
    def get(self, request, *args, **kwargs):
        p = Proyectos.objects.get(id=self.kwargs['id'])
        solicitudes = solicitudCambio.objects.filter(item__fase__proyecto = p).order_by('id')
        import os
        # Obtenemos de platypus las clases Paragraph, para escribir parrafos Image, para insertar imagenes y SimpleDocTemplate para definir el DocTemplate. Ademas importamos Spacer, para incluir espacios .
        from reportlab.platypus import Paragraph
        from reportlab.platypus import Image
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.platypus import Spacer
        from reportlab.platypus import Table

        # Importamos clase de hoja de estilo de ejemplo.
        from reportlab.lib.styles import getSampleStyleSheet

        # Se importa el tamanho de la hoja y los colores
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors

        # Creamos un PageTemplate de ejemplo.
        estiloHoja = getSampleStyleSheet()

        #Inicializamos la lista Platypus Story.
        story = []

        #Definimos como queremos que sea el estilo de la PageTemplate.
        print estiloHoja
        cabecera = estiloHoja['Heading4']

        #No se hara un salto de pagina despues de escribir la cabecera (valor 1 en caso contrario).
        cabecera.pageBreakBefore=0

        # Se quiere que se empiece en la primera pagina a escribir. Si es distinto de 0 deja la primera hoja en blanco.
        cabecera.keepWithNext=0

        # Color de la cabecera.
        cabecera.backColor=colors.lightblue

        # Ahora incluimos una imagen.
        fichero_imagen = IMAGENES_ROOT + "/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen),width=400,height=100)
        story.append(imagen_logo)

        # Incluimos un Flowable, que en este caso es un parrafo.
        parrafo = Paragraph("Solicitudes de cambio",cabecera)
        # Lo incluimos en el Platypus story.
        story.append(parrafo)

        # Definimos un parrafo. Vamos a crear un texto largo para demostrar como se genera mas de una hoja.
        lista = []
        lista.append(['Id','Linea Base','Descricipcion','Estado','Solicitante', 'Costo', 'Lider Voto'])
        fas = fases.objects.filter(proyecto=p)
        for s in solicitudes:
            voto=votos.objects.get(solicitud=s, usuario=p.lider)
            if(voto.estado=='pendiente'):
                votolider = 'No'
            else:
                votolider = 'Si'
            lista.append([s.id,s.lineaBase.nombre ,s.descripcion, s.estado, s.usuario, s.costoAdicional, votolider])
        t=Table( lista, style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                       ('BOX',(0,0),(-1,-1),2,colors.black),
                       ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                       ]
              )
        # Y lo incluimos en el story.
        story.append(t)

        # Dejamos espacio.
        story.append(Spacer(0,20))

        # Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc=SimpleDocTemplate(MEDIA_ROOT + "/solicitud_" +str(s.id) + ".pdf",pagesize=A4,showBoundary=1)

        # Construimos el Platypus story.
        doc.build(story)
        image_data = open(MEDIA_ROOT + "/solicitud_" +str(s.id) + ".pdf", "rb").read()
        return HttpResponse(image_data, mimetype="application/pdf")