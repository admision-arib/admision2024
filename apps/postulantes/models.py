import os
from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()


#class Persona(models.Model):
#    """Model definition for Persona."""
#
#    # TODO: Define fields here
#    nombre = models.CharField(max_length=100)
#    apellidos = models.CharField(max_length=100)
#    dni = models.CharField(max_length=8)
#    correo = models.EmailField(max_length=254)
#    fecha_registro = models.DateTimeField(auto_now_add=True)
#
#    class Meta:
#        """Meta definition for Persona."""
#
#        verbose_name = 'Persona'
#        verbose_name_plural = 'Personas'
#
#    def __str__(self):
#        """Unicode representation of Persona."""
#        return f"{self.nombre} {self.apellidos}"


class Postulante(models.Model):
    """Model definition for Postulante."""
    GENERO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    CARRERAS_CHOICES = (
        ('C', 'Contabilidad'),
        ('EM', 'Explotación Minera'),
        ('CC', 'Construcción Civil'),
    )

    # TODO: Define fields here
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno  = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    correo = models.EmailField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    celular = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    lugar_nacimiento = models.CharField(max_length=100)
    lugar_nacimiento_distrito = models.CharField(max_length=100, verbose_name='Distrito')
    lugar_nacimiento_provincia = models.CharField(max_length=100, verbose_name = 'Provincia')
    lugar_nacimiento_departamento = models.CharField(max_length=100, verbose_name = 'Departamento')
    tutor_apellidos = models.CharField(max_length=100, blank=True)
    tutor_nombres = models.CharField(max_length=100, blank=True)
    tutor_parentesco = models.CharField(max_length=100, blank=True)
    nombre_ies = models.CharField(max_length=100)
    tipo_institucion = models.CharField(max_length=20, choices=(('Publica', 'Publica'), ('Privada', 'Privada')))
    anio_egreso = models.CharField(verbose_name = 'Año_egreso', max_length=4)
    direccion_institucion = models.CharField(max_length=255)
    institucion_distrito = models.CharField(max_length=100)
    institucion_provincia = models.CharField(max_length=100)
    institucion_departamento = models.CharField(max_length=100)
    programa_postula_primera_opcion = models.CharField(max_length=2, choices=CARRERAS_CHOICES)
    programa_postula_segunda_opcion = models.CharField(max_length=2, choices=CARRERAS_CHOICES)
    enterado_proceso_admision = models.CharField(max_length=100, verbose_name= '¿Cómo se entero del proceso de admisión?')
    codigo_voucher = models.CharField(max_length=15, unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    imagen1 = models.FileField('DNI', upload_to='maps', blank=False, null=False, storage=gd_storage)
    imagen2 = models.FileField('Certificado de Estudios', upload_to='maps', blank=False, null=False, storage=gd_storage)
    imagen3 = models.FileField('Partida de Nacimiento', upload_to='maps', blank=False, null=False, storage=gd_storage)
    imagen4 = models.FileField('Voucher', upload_to='maps', blank=False, null=False, storage=gd_storage)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Postulante'
        verbose_name_plural = 'Postulantes'
    

    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.dni
    

#class Documento(models.Model):
#    """Model definition for MODELNAME."""
#    #DOCUMENTO_CHOICES = (
#    #    ('DNI', 'DNI'),
#    #    ('V', 'VOUCHER DE PAGO'),
#    #    ('CE', 'CERTIFICADO DE ESTUDIOS'),
#    #    ('PN', 'PARTIDA O CONSTANCIA DE NACIMIENTO')
#    #)
#    # TODO: Define fields here
#    postulante = models.ForeignKey(Postulante, on_delete=models.CASCADE)
#    imagen = models.ImageField(upload_to='documentos/')
#    fecha_creacion = models.DateTimeField(auto_now_add=True) # URL de la imagen en Google Drive
#    # Otros campos relevantes para la gestión de documentos del postulante
#
#    class Meta:
#        """Meta definition for MODELNAME."""
#
#        verbose_name = 'Documento'
#        verbose_name_plural = 'Documentos'
#
#    def __str__(self):
#        """Unicode representation of MODELNAME."""
#        return f"Documento de {self.postulante} ({self.fecha_creacion})"



