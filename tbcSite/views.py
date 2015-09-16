from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from usuarios.models import Usuario, ReservaMobiBus
from tranvias.models import ConductorTranvia, Tranvia, Linea, AlertaTranvia, CoordenadasTranvia
from movibuses.models import ConductorMoviBus, MoviBus, CoordenadasMoviBus
from vcubs.models import EstacionVcub, Vcub
from reportes.models import ReporteMoviBus, ReporteTranvia
from tbcSite.serializers import UsuarioSerializer, ReservaMobiBusSerializer, ConductorTranviaSerializer, TranviaSerializer, LineaSerializer, AlertaTranviaSerializer. ConductorTranviaSerializer, ConductorMoviBusSerializer, MoviBusSerializer, CoordenadasMoviBusSerializer, EstacionVcubSerializer, VcubSerializer,ReporteTranviaSerializer, ReporteMoviBusSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

    @csrf_exempt
    def usuario_list(request):
        if request.method == 'GET':
            usuarios = Usuario.objects.all()
            serializer = UsuarioSerializer(usuarios, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = UsuarioSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def reservasMobiBus_list(request):
        if request.method == 'GET':
            reservasMobiBus = ReservaMobiBus.objects.all()
            serializer = ReservaMobiBusSerializer(reservasMobiBus, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ReservaMobiBusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def conductoresTranvia_list(request):
        if request.method == 'GET':
            conductoresTranvia = ConductorTranvia.objects.all()
            serializer = ConductorTranviaSerializer(conductoresTranvia, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ConductorTranviaBusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def tranvias_list(request):
        if request.method == 'GET':
            tranvias = Tranvia.objects.all()
            serializer = TranviaSerializer(tranvias, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = TranviaBusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def coordenadasTranvia_list(request):
        if request.method == 'GET':
            coordenadasTranvia = CoordenadasTranvia.objects.all()
            serializer = CoordenadasTranviaSerializer(coordenadasTranvia, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CoordenadasTranviaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def lineas_list(request):
        if request.method == 'GET':
            lineas = Linea.objects.all()
            serializer = LineaSerializer(lineas, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = LineaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def alertasTranvia_list(request):
        if request.method == 'GET':
            alertasTranvia = AlertaTranvia.objects.all()
            serializer = AlertaTranviaSerializer(alertasTranvia, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = AlertaTranviaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def conductoresMoviBus_list(request):
        if request.method == 'GET':
            conductoresMoviBus = ConductorMoviBus.objects.all()
            serializer = ConductorTranviaSerializer(conductoresMoviBus, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ConductorTranviaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def moviBuses_list(request):
        if request.method == 'GET':
            moviBuses = MoviBus.objects.all()
            serializer = MoviBusSerializer(moviBuses, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = MoviBusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def coordenadasMoviBus_list(request):
        if request.method == 'GET':
            coordenadasMoviBus = CoordenadasMoviBus.objects.all()
            serializer = CoordenadasMoviBusSerializer(coordenadasMoviBus, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CoordenadasMoviBus(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def estacionesVcubs_list(request):
        if request.method == 'GET':
            estacionesVcubs = EstacionVcub.objects.all()
            serializer = EstacionVcubSerializer(estacionesVcubs, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = EstacionVcubSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def vcubs_list(request):
        if request.method == 'GET':
            vcubs = Vcub.objects.all()
            serializer = VcubSerializer(vcubs, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = VcubSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def reportesMoviBus_list(request):
        if request.method == 'GET':
            reportesMoviBus = ReporteMoviBus.objects.all()
            serializer = ReporteMoviBusSerializer(reportesMoviBus, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ReporteMoviBusSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def reportesTranvia_list(request):
        if request.method == 'GET':
            reportesTranvia = ReporteTranvia.objects.all()
            serializer = ReporteTranviaSerializer(reportesTranvia, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = ReporteTranviaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def usuario_detail(request, pk):
        try:
            usuario = Usuario.objects.get(pk=login)
        except Usuario.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = UsuarioSerializer(usuario)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = UsuarioSerializer(usuario, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            usuario.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def reservaMobiBus_detail(request, pk):
        try:
            reservaMobiBus = ReservaMobiBus.objects.get(pk=unique_together)
        except reservaMobiBus.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ReservaMobiBusSerializer(reservaMobiBus)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ReservaMobiBusSerializer(reservaMobiBus, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            reservaMobiBus.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def conductorTranvia_detail(request, pk):
        try:
            conductorTranvia = ConductorTranvia.objects.get(pk=cedula)
        except conductorTranvia.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ConductorTranviaSerializer(conductorTranvia)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ConductorTranviaSerializer(conductorTranvia, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            conductorTranvia.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def tranvia_detail(request, pk):
        try:
            tranvia = Tranvia.objects.get(pk=placa)
        except tranvia.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = TranviaSerializer(tranvia)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = TranviaSerializer(tranvia, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            tranvia.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def coordenadasTranvia_detail(request, pk):
        try:
            coordenadasTranvia = CoordenadasTranvia.objects.get(pk=unique_together)
        except coordenadasTranvia.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = CoordenadasTranviaSerializer(coordenadasTranvia)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CoordenadasTranviaSerializer(coordenadasTranvia, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            coordenadasTranvia.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def linea_detail(request, pk):
        try:
            linea = Linea.objects.get(pk=numero)
        except linea.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = LineaSerializer(linea)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = LineaSerializer(linea, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            linea.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def alertaTranvia_detail(request, pk):
        try:
            alertaTranvia = AlertaTranvia.objects.get(pk=unique_together)
        except alertaTranvia.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = AlertaTranviaSerializer(alertaTranvia)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = AlertaTranviaSerializer(alertaTranvia, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            alertaTranvia.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def conductorMoviBus_detail(request, pk):
        try:
            conductorMoviBus = ConductorMoviBus.objects.get(pk=cedula)
        except conductorMoviBus.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ConductorMoviBusSerializer(conductorMoviBus)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ConductorMoviBusSerializer(conductorMoviBus, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            conductorMoviBus.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def moviBus_detail(request, pk):
        try:
            moviBus = MoviBus.objects.get(pk=placa)
        except moviBus.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = MoviBusSerializer(moviBus)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = MoviBusSerializer(moviBus, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            moviBus.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def coordenadasMoviBus_detail(request, pk):
        try:
            coordenadasMoviBus = CoordenadasMoviBus.objects.get(pk=unique_together)
        except coordenadasMoviBus.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = CoordenadasMoviBusSerializer(coordenadasMoviBus)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = CoordenadasMoviBusSerializer(coordenadasMoviBus, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            coordenadasMoviBus.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def estacionesVcubs_detail(request, pk):
        try:
            estacionesVcubs = EstacionVcub.objects.get(pk=nombre)
        except estacionesVcubs.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = EstacionVcubSerializer(estacionesVcubs)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = EstacionVcubSerializer(estacionesVcubs, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            estacionesVcubs.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def vcubs_detail(request, pk):
        try:
            vcubs = Vcub.objects.get(pk=registro)
        except vcubs.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = VcubSerializer(vcubs)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = VcubSerializer(vcubs, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            vcubs.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def reportesMoviBus_detail(request, pk):
        try:
            reportesMoviBus = ReporteMoviBus.objects.get(pk=unique_together)
        except reportesMoviBus.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ReporteMoviBusSerializer(reportesMoviBus)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ReporteMoviBusSerializer(reportesMoviBus, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            reportesMoviBus.delete()
            return HttpResponse(status=204)

    @csrf_exempt
    def reportesTranvia_detail(request, pk):
        try:
            reportesTranvia = ReporteTranvia.objects.get(pk=unique_together)
        except reportesTranvia.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = ReporteTranviaSerializer(reportesTranvia)
            return JSONResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = ReporteTranviaSerializer(reportesTranvia, data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data)
            return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            reportesTranvia.delete()
            return HttpResponse(status=204)
