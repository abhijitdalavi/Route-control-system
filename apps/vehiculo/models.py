from django.db import models
from apps.conductor.models import Conductor


class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=6)
    conductorDefault = models.ForeignKey(Conductor, blank=True, null=True, on_delete=models.CASCADE)
    numeroInterno = models.CharField(max_length=6)
    combustible = models.CharField(max_length=10)
    logo = models.ImageField(blank=True, null=True, upload_to="vehiculo_media")
    numLicenciaTransito = models.IntegerField()
    docLicenciaTransito = models.FileField(blank=True, null=True, upload_to="licenciaTransito_media")
    organismoTransito = models.TextField()
    fechaExpedicion = models.DateField()
    marca = models.CharField(max_length=15)
    linea = models.CharField(max_length=15)
    cilindraje = models.IntegerField()
    modelo = models.IntegerField()
    claseVehiculo = models.CharField(max_length=15)
    color = models.CharField(max_length=30)
    tipoServicio = models.CharField(max_length=20)
    carroceria = models.CharField(max_length=15)
    capacidad = models.IntegerField()
    numMotor = models.TextField()
    numChasis = models.TextField()
    propietario = models.TextField()
    idPropietario = models.IntegerField()
    numTarjetaOperacion = models.CharField(max_length=15)
    docTO = models.FileField(blank=True, null=True, upload_to="TarjetasOperacion_media")
    fechaInicioTo = models.DateField()
    fechaVencimientoTo = models.DateField()
    empresaAfiliado = models.TextField()
    idEmpresaAfiliado = models.IntegerField()
    numSoat = models.CharField(max_length=15)
    docSoat = models.FileField(blank=True, null=True, upload_to="Soat_media")
    fechaInicioSoat = models.DateField()
    fechaVencimientoSoat = models.DateField()
    aseguradoraSoat = models.TextField()
    numCertificadoRtm = models.CharField(max_length=15)
    docRtm = models.FileField(blank=True, null=True, upload_to="RevisionTecnicoMecanica_media")
    fechaInicioRtm = models.DateField()
    fechaVencimientoRtm = models.DateField()
    cda = models.TextField()
    numeroPolizasRce_Rcc = models.CharField(max_length=15, blank=True, null=True)
    docPolizasRce_Rcc = models.FileField(blank=True, null=True, upload_to="PolizasRcc_Rce_media")
    fechaInicioRce_Rcc = models.DateField()
    fechaVencimientoRce_Rcc = models.DateField()
    aseguradoraRce_Rcc = models.TextField()
    activo_inactivo = models.BooleanField(blank=True, default=True)