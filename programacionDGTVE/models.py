from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

#Atributos
class Atributo(models.Model):
    nombre = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Atributo'
        verbose_name_plural = 'Atributos'

class Clasificacion(models.Model):
    clave = models.CharField(max_length=5, null=True, blank=True)
    descClasificacion = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.clave
    
    class Meta:
        verbose_name = 'Clasificacion'
        verbose_name_plural = 'Clasificaciones'

class Canal(models.Model):

    nombreCanal = models.CharField(max_length=50, null=False, blank=False)
    numeroCanal = models.IntegerField(null=False, blank=False)
    logo = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name = 'Canal'
        verbose_name_plural = 'Canales'

    def __str__(self):
        return self.nombreCanal
    
class Barra(models.Model):

    desBarra = models.CharField(max_length=50, null=False, blank=False)
    abreviatura = models.CharField(max_length=20, null=True, blank=False)

    class Meta:
        verbose_name = 'Barra'
        verbose_name_plural = 'Barras'
    
    def __str__(self):
        return self.name

class DetalleSerie(models.Model):

    materia = models.CharField(max_length=50, null=False, blank=False)
    nivelEducativo = models.CharField(max_length=50, null=False, blank=False)
    grado = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = 'Detalle Serie'
        verbose_name_plural = 'Detalle Series'

    def __str__(self):
        return self.materia
    
class TipoSerie(models.Model):

    nombreSerie = models.CharField(max_length=50, null=False, blank=False)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Tipo Serie'
        verbose_name_plural = 'Tipo Series'

    def __str__(self):
        return self.nombre_serie

class Serie(models.Model):
    nombreSerie = models.CharField(max_length=150, null=False, blank=False)
    sinopsis = models.CharField(max_lenght=150, null=True, blank=True)
    anioProduccion = models.DateField(null=False, blank=False)
    duracion = models.TimeField(null=False, blank=False)
    formatoCinta = models.CharField(max_length=20)
    observaciones = models.CharField(max_length=150, null=True, blank=True)
    detalleSerie_id = models.ForeignKey(DetalleSerie, on_delete=models.CASCADE, null=False, blank=False)
    tipoSerie_id = models.ForeignKey(TipoSerie, on_delete=models.CASCADE, null=False, blank=False)


    def __str__(self):
        return self.nombreSerie

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'

class Programa(models.Model):

    folioCinta = models.IntegerField(null=False, blank=False)
    programa = models.CharField(max_length=150)
    codigoBarra = models.CharField(max_length=12, null=False, blank= False)
    videoTipo = models.CharField(max_length=5, null=False, blank=False)
    condicionTrans = models.CharField(max_length=150, null=False, blank=False)
    fechaCalificacion = models.DateField(auto_now=False, auto_now_add=False)
    tx = models.CharField(max_length=5, null=False, blank=False)
    fechaMovimiento = models.DateTimeField(auto_now=True, auto_now_add=False)
    usuarioMovimiento = models.CharField(max_length=20)
    pasadas = models.CharField(max_length=5, null=False, blank=False)
    serieInternoExterno = models.IntegerField(null=False, blank=False)
    subtitulo = models.CharField(max_length=100)
    fechaModificacionVideoteca = models.DateTimeField(auto_now=True, auto_now_add=False)
    institucionProductora = models.CharField(max_length=300)
    productor = models.CharField(max_length=60)
    fechaUltimoMovimiento = models.DateTimeField(auto_now=False, auto_now_add=False)
    usuarioUltimoMovimiento = models.CharField(max_length=20)
    statusFusion = models.BooleanField(default=True)
    fechaVigencia = models.DateTimeField(auto_now=False, auto_now_add=False)
    canal_id = models.ForeignKey(Canal, on_delete=models.CASCADE, null=False, blank=False)
    clasificacion_id = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, null=False, blank=False)
    atributo_id = models.ForeignKey(Atributo, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return self.programa

class Programacion(models.Model):

    fechaPrograma = models.DateField(auto_now=False, auto_now_add=False)
    horaInicial = models.TimeField(auto_now=False, auto_now_add=False)
    horaFinal = models.TimeField(auto_now=False, auto_now_add=False)
    bloque = models.CharField(max_length=20, null=False, blank=False)
    secuencia = models.CharField(max_length=20, null=False, blank=False)
    observacionesTransmision = models.CharField(max_length=150, null=False, blank=False)
    statusTransmision = models.IntegerField(null=False, blank=False)
    observaTransmision = models.CharField(max_length=150, null=False, blank=False)
    duracion = models.TimeField(auto_now=False, auto_now_add=False)
    numEnvio = models.IntegerField(null=False, blank=False)
    fechaEnvio = models.DateTimeField(auto_now=False, auto_now_add=False)
    usuarioEnvio = models.CharField(max_length=20, null=False, blank=False)
    reprogramado = models.IntegerField(null=False, blank=False)
    colorHexadecimal = models.CharField(max_length=7)
    nomCanal = models.CharField(max_length=50, null=False, blank=False)
    subtitulaje = models.BooleanField(default = False)
    fechaEnterado = models.DateTimeField(auto_now=False, auto_now_add=False)
    observacionAviso = models.CharField(max_length=150)
    programacionEliminada = models.BooleanField(default=False)
    programacionAPasos = models.BooleanField(default=False)
    programa_id = models.ForeignKey(Programa, on_delete=models.CASCADE, null=False, blank=False)
    canal_id = models.ForeignKey(Canal, on_delete=models.CASCADE, null=False, blank=False)
    barra_id = models.ForeignKey(Barra, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'

    def __str__(self):
        return self.fechaPrograma
    
class DetalleProgramacion(models.Model):

    tipoAcepta = models.CharField(max_length=50, null=False, blank=False) # I, O, V, I1, I2, I3 ... ETC
    fechaAceptaEnvio = models.DateTimeField(auto_now=False, auto_now_add=False)
    usuarioAceptaEnvio = models.CharField(max_length=20, null=False, blank=False)
    obsRecepcionProgramacion = models.CharField(max_length=150, null=False, blank=False)
    statusAceptaEnvio = models.BooleanField(default=False)
    statusRevisado = models.BooleanField(default=False)
    enterado = models.BooleanField(default=False)
    programacion_id = models.ForeignKey(Programacion, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'Detalle Programacion'
        verbose_name_plural = 'Detalles Programacion'

    def __str__(self):
        return self.tipoAcepta
