from django.test import TestCase
from tienda.models import Orden
from datetime import datetime
from django.utils import timezone
import zoneinfo
# Create your tests here.
class TiendaViewsTests(TestCase):

    def test_v_index(self):
        
        '''
            Debe entregar todos los registros sin no existen filtros
        '''
        respuesta = self.client.get("/") #todo el texto visual del front lo guardo en esta variable
        ords = respuesta.context["ordenes"]
        self.assertEqual(0, len(ords))

        nuevo = Orden()
        nuevo.cliente ="Sebastian"
        nuevo.fecha = "2023-12-12"
        nuevo.fecha_envio = "2023-12-15"
        nuevo.direccion = "El Arrayan"
        nuevo.save()
        
        respuesta = self.client.get("/") 
        ords = respuesta.context["ordenes"]
        self.assertEqual(1, len(ords))

    def test_v_index_filtros(self):
            '''
                Entrega los registros con filtros de fecha
            '''
        
            nuevo = Orden()
            nuevo.cliente ="Carlos"
            nuevo.fecha = "2022-12-15"
            nuevo.fecha_envio = datetime(2022, 12, 15).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
            nuevo.direccion = "El Arrayan"
            nuevo.save()

            nuevo = Orden()
            nuevo.cliente ="Marcelo"
            nuevo.fecha = "2023-12-12"
            nuevo.fecha_envio = datetime(2023, 12, 15).astimezone(zoneinfo.ZoneInfo('America/Santiago'))
            nuevo.direccion = "Av. Grecia"
            nuevo.save()

            res = self.client.get("/?fecha_inicio=%s&fecha_fin=%s" % (
                '2023-11-01', '2023-12-25'))

            ords = res.context["ordenes"]
            self.assertEqual(1, len(ords))






        #print("Test 1")
        #print("----->>>", Orden.objects.all().count())