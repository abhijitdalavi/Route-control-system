from django.db import models
from apps.conductor.models import Conductor


class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=6)
    conductor_default = models.ForeignKey(Conductor, blank=True, null=True, on_delete=models.CASCADE)
    numero_interno = models.CharField(max_length=6)
    combustible = models.CharField(max_length=10)
    logo = models.ImageField(blank=True, null=True, upload_to="vehiculo_media")
    num_licencia_transito = models.IntegerField()
    doc_licencia_transito = models.FileField(blank=True, null=True, upload_to="licenciaTransito_media")
    organismo_transito = models.TextField()
    fecha_expedicion = models.DateField()
    marca = models.CharField(max_length=15)
    linea = models.CharField(max_length=15)
    cilindraje = models.IntegerField()
    modelo = models.IntegerField()
    clase_vehiculo = models.CharField(max_length=15)
    color = models.CharField(max_length=30)
    tipo_servicio = models.CharField(max_length=20)
    carroceria = models.CharField(max_length=15)
    capacidad = models.IntegerField()
    num_motor = models.TextField()
    num_chasis = models.TextField()
    propietario = models.TextField()
    id_propietario = models.IntegerField()
    num_tarjeta_operacion = models.CharField(max_length=15)
    doc_to = models.FileField(blank=True, null=True, upload_to="TarjetasOperacion_media")
    fecha_inicio_to = models.DateField()
    fecha_vencimiento_to = models.DateField()
    empresa_afiliado = models.TextField()
    id_empresa_afiliado = models.IntegerField()
    num_soat = models.CharField(max_length=15)
    doc_soat = models.FileField(blank=True, null=True, upload_to="Soat_media")
    fecha_inicio_soat = models.DateField()
    fecha_vencimiento_soat = models.DateField()
    aseguradora_soat = models.TextField()
    num_certificado_rtm = models.CharField(max_length=15)
    doc_rtm = models.FileField(blank=True, null=True, upload_to="RevisionTecnicoMecanica_media")
    fecha_inicio_rtm = models.DateField()
    fecha_vencimiento_rtm = models.DateField()
    cda = models.TextField()
    numero_polizas_rce_rcc = models.CharField(max_length=15, blank=True, null=True)
    doc_polizas_rce_rcc = models.FileField(blank=True, null=True, upload_to="PolizasRcc_Rce_media")
    fecha_inicio_rce_rcc = models.DateField()
    fecha_vencimiento_rce_rcc = models.DateField()
    aseguradora_rce_rcc = models.TextField()
    activo_inactivo = models.BooleanField(blank=True, default=True)
