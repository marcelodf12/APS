from django.shortcuts import render
from django.views.generic import TemplateView
from aps.aplicaciones.proyectos.models import Proyectos
from aps.aplicaciones.fases.models import fases
from aps.aplicaciones.solicitudCambio.models import solicitudCambio, votos
from aps.aplicaciones.items.models import items, relacion
from django.http import HttpResponse
from aps.settings import MEDIA_ROOT, IMAGENES_ROOT
# Create your views here.

class reporteItems(TemplateView):
    template_name = 'reportes/proyecto.html'
    def get(self, request, *args, **kwargs):
        p = Proyectos.objects.get(id=self.kwargs['id'])
        import os
        # Obtenemos de platypus las clases Paragraph, para escribir parrafos Image, para insertar imagenes y SimpleDocTemplate para definir el DocTemplate. Ademas importamos Spacer, para incluir espacios .
        from reportlab.platypus import Paragraph
        from reportlab.platypus import Image
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.platypus import Spacer
        from reportlab.platypus import Table
        from reportlab.lib import styles

        # Importamos clase de hoja de estilo de ejemplo.
        from reportlab.lib.styles import getSampleStyleSheet

        # Se importa el tamanho de la hoja y los colores
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors

        # Creamos un PageTemplate de ejemplo.
        estiloHoja = getSampleStyleSheet()

        #Inicializamos la lista Platypus Story.
        story = []
        # Ahora incluimos una imagen.
        fichero_imagen = IMAGENES_ROOT + "/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen),width=400,height=50)
        story.append(imagen_logo)


        #Definimos como queremos que sea el estilo de la PageTemplate.
        cabecera = estiloHoja['Heading5']

        #No se hara un salto de pagina despues de escribir la cabecera (valor 1 en caso contrario).
        cabecera.pageBreakBefore=0

        # Se quiere que se empiece en la primera pagina a escribir. Si es distinto de 0 deja la primera hoja en blanco.
        cabecera.keepWithNext=0



        # Color de la cabecera.
        cabecera.backColor=colors.white
        cabecera.spaceAfter = 0
        cabecera.spaceBefore = 0

        parrafo = Paragraph('.',cabecera)
        story.append(parrafo)
        parrafo = Paragraph('Proyecto: '+ p.nombre,cabecera)
        story.append(parrafo)
        parrafo = Paragraph('-'*193,cabecera)
        story.append(parrafo)

        # Incluimos un Flowable, que en este caso es un parrafo.

        cabecera2 = estiloHoja['Heading3']
        cabecera2.pageBreakBefore=0
        cabecera2.keepWithNext=0
        cabecera2.backColor=colors.white

        parrafo = Paragraph('   ',cabecera2)
        # Lo incluimos en el Platypus story.
        story.append(parrafo)

        # Definimos un parrafo. Vamos a crear un texto largo para demostrar como se genera mas de una hoja.

        fas = fases.objects.filter(proyecto=p)
        for f in fas:
            li = items.objects.filter(fase=f).order_by('id')
            lista = []
            lista.append(['FASE: ' + f.nombre])
            lista.append(['ID','DESCRIPCION','PADRE','VERSION','COSTO', 'ESTADO'])
            for i in li:
                padre = 'No tiene'
                r = relacion.objects.filter(itemHijo=i)
                if r:
                    for aux in r:
                        padre = aux.itemPadre.nombre
                lista.append([i.id,i.nombre,padre,i.versionAct,i.costo,i.estado])
            lista.append([''])
            t=Table( lista, style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.white),
                       ('BOX',(0,0),(-1,-1),2,colors.white),
                       ('SPAN',(0,0),(-1,0)),
                       ('ROWBACKGROUNDS', (0, 2), (-1, -1), (colors.Color(0.9, 0.9, 0.9),colors.white)),
                       ('BACKGROUND', (0, 1), (-1, 1), colors.rgb2cmyk(r=6,g=62,b=193)),
                       ('LINEABOVE',(0,0),(-1,0),1.5,colors.black),
                       ('LINEBELOW',(0,0),(-1,0),1.5,colors.black),
                       ('SIZE',(0,0),(-1,0),12),
                       ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                       ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                       ('TEXTCOLOR', (0, 1), (-1, 1), colors.white),
                       ('BACKGROUND', (0, -1), (-1, -1), colors.white),
                       ]
              )
            # Y lo incluimos en el story.
            story.append(t)


        # Dejamos espacio.
        story.append(Spacer(0,20))

        # Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc=SimpleDocTemplate(MEDIA_ROOT + "/proyecto_" +str(p.id) + ".pdf",pagesize=A4, rightMargin=1, leftMargin=1, topMargin=0, bottomMargin=0)
        import datetime

        parrafo = Paragraph('-'*193,cabecera)
        story.append(parrafo)
        print 'a' + ' '*100 + 'b'
        parrafo = Paragraph('Fin del Informe' + ' '*100 + '('+str(datetime.date.today()) + ')' ,cabecera)
        story.append(parrafo)



        # Construimos el Platypus story.
        doc.build(story)

        image_data = open(MEDIA_ROOT + "/proyecto_" +str(p.id) + ".pdf", "rb").read()
        return HttpResponse(image_data, mimetype="application/pdf")


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
        from reportlab.lib import styles

        # Importamos clase de hoja de estilo de ejemplo.
        from reportlab.lib.styles import getSampleStyleSheet

        # Se importa el tamanho de la hoja y los colores
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors

        # Creamos un PageTemplate de ejemplo.
        estiloHoja = getSampleStyleSheet()

        #Inicializamos la lista Platypus Story.
        story = []
        # Ahora incluimos una imagen.
        fichero_imagen = IMAGENES_ROOT + "/cabecera.png"
        imagen_logo = Image(os.path.realpath(fichero_imagen),width=400,height=50)
        story.append(imagen_logo)


        #Definimos como queremos que sea el estilo de la PageTemplate.
        cabecera = estiloHoja['Heading5']

        #No se hara un salto de pagina despues de escribir la cabecera (valor 1 en caso contrario).
        cabecera.pageBreakBefore=0

        # Se quiere que se empiece en la primera pagina a escribir. Si es distinto de 0 deja la primera hoja en blanco.
        cabecera.keepWithNext=0



        # Color de la cabecera.
        cabecera.backColor=colors.white
        cabecera.spaceAfter = 0
        cabecera.spaceBefore = 0

        parrafo = Paragraph('.',cabecera)
        story.append(parrafo)
        parrafo = Paragraph('Proyecto: '+ p.nombre,cabecera)
        story.append(parrafo)
        parrafo = Paragraph('-'*193,cabecera)
        story.append(parrafo)

        # Incluimos un Flowable, que en este caso es un parrafo.

        cabecera2 = estiloHoja['Heading3']
        cabecera2.pageBreakBefore=0
        cabecera2.keepWithNext=0
        cabecera2.backColor=colors.white

        parrafo = Paragraph('   ',cabecera2)
        # Lo incluimos en el Platypus story.
        story.append(parrafo)

        # Definimos un parrafo. Vamos a crear un texto largo para demostrar como se genera mas de una hoja.
        lista = []
        lista.append(['SOLICITUDES DE CAMBIO','','','','', '', ''])
        lista.append([' ',' ',' ',' ',' ', ' ', ' '])
        lista.append(['ID','LINEA BASE','DESCRIPCION','ESTADO','SOLICITANTE', 'COSTO', 'LIDER VOTO?'])
        fas = fases.objects.filter(proyecto=p)
        for s in solicitudes:
            voto=votos.objects.get(solicitud=s, usuario=p.lider)
            if(voto.estado=='pendiente'):
                votolider = 'No'
            else:
                votolider = 'Si'
            lista.append([s.id,s.lineaBase.nombre ,s.descripcion, s.estado, s.usuario, s.costoAdicional, votolider])
        t=Table( lista, style = [
                       ('GRID',(0,0),(-1,-1),0.5,colors.white),
                       ('BOX',(0,0),(-1,-1),2,colors.white),
                       ('SPAN',(0,0),(-1,0)),
                       ('ROWBACKGROUNDS', (0, 3), (-1, -1), (colors.Color(0.9, 0.9, 0.9),colors.white)),
                       ('BACKGROUND', (0, 2), (-1, 2), colors.rgb2cmyk(r=6,g=62,b=193)),
                       ('BACKGROUND', (0, 1), (-1, 1), colors.white),
                       ('LINEABOVE',(0,0),(-1,0),1.5,colors.black),
                       ('LINEBELOW',(0,0),(-1,0),1.5,colors.black),
                       ('SIZE',(0,0),(-1,0),12),
                       ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                       ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
                       ('TEXTCOLOR', (0, 2), (-1, 2), colors.white),
                       ]
              )
        # Y lo incluimos en el story.
        story.append(t)

        # Dejamos espacio.
        story.append(Spacer(0,20))

        # Creamos un DocTemplate en una hoja DIN A4, en la que se muestra el texto enmarcado (showBoundary=1) por un recuadro.
        doc=SimpleDocTemplate(MEDIA_ROOT + "/solicitud_" +str(p.id) + ".pdf",pagesize=A4, rightMargin=1, leftMargin=1, topMargin=0, bottomMargin=0)
        import datetime

        parrafo = Paragraph('-'*193,cabecera)
        story.append(parrafo)
        print 'a' + ' '*100 + 'b'
        parrafo = Paragraph('Fin del Informe' + ' '*100 + '('+str(datetime.date.today()) + ')' ,cabecera)
        story.append(parrafo)



        # Construimos el Platypus story.
        doc.build(story)

        image_data = open(MEDIA_ROOT + "/solicitud_" +str(p.id) + ".pdf", "rb").read()
        return HttpResponse(image_data, mimetype="application/pdf")

class menu(TemplateView):
    def get(self, request, *args, **kwargs):
        proyectos = Proyectos.objects.filter(lider=request.user)
        return render(self.request, 'reportes/proyecto.html', {'proyectos':proyectos})