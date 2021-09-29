from django.db import models
from datetime import datetime

DIA_CHOICE = (
    ('Lu', 'Lunes'),
    ('Ma', 'Martes'),
    ('Mi', 'Miércoles'),
    ('Ju', 'Jueves'),
    ('Vi', 'Viernes')
)


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    cp = models.IntegerField("Código Postal", primary_key=True)

    class Meta:
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return '%s CP %s' % (self.nombre, self.cp)


class Persona(models.Model):
    num_doc = models.IntegerField("Número de Documento", primary_key=True, unique=True)
    nombre = models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=150)
    num_cuit = models.CharField("Número de CUIT/CUIL", max_length=20, null=True, blank=True)
    fecha_nac = models.DateField("Fecha de nacimiento", default=datetime.now)
    telefono = models.CharField("Número de teléfono", max_length=50)
    email = models.EmailField("E-mail", max_length=100)
    direccion = models.CharField("Dirección", max_length=120)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="persona_localidad")

    class Meta:
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)


class Usuario(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="usuario_persona")
    nombre = models.CharField("Nombre de usuario", max_length=50, primary_key=True, unique=True)
    password = models.CharField("Contraseña", max_length=8)

    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    paciente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    num_hc = models.IntegerField("Número de historia clínica", primary_key=True, unique=True)
    num_os = models.IntegerField("Número de Obra Social", null=True, blank=True)
    titular = models.BooleanField("¿Titular?")

    def __str__(self):
        return '%s, %s, %s' % (self.paciente, self.num_hc, self.titular)


class Profesional(models.Model):
    profesional = models.ForeignKey(Persona, on_delete=models.PROTECT)
    matricula = models.IntegerField("Número de matrícula", primary_key=True, unique=True)
    especialidad = models.CharField(max_length=150)

    def __str__(self):
        return '%s, %s, %s' % (self.profesional, self.matricula, self.especialidad)


class ObraSocial(models.Model):
    nombreOS = models.CharField("Obra Social", primary_key=True, max_length=254)
    direccion = models.CharField("Dirección de la Obra Social", max_length=120)
    disponible = models.BooleanField("Disponible")

    def __str__(self):
        return self.nombreOS


class Turno(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, primary_key=True)
    medico = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    fecha = models.DateTimeField("Fecha del turno")
    estado = models.CharField("Estado", max_length=30)

    class Meta:
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return '%s, %s, %s' % (self.paciente, self.medico, self.fecha)


class Establecimiento(models.Model):
    nombre = models.CharField("Nombre del establecimiento", max_length=150, primary_key=True)
    razon_social = models.CharField("Razón social", max_length=150)
    direccion = models.CharField(max_length=120)
    localidad = models.ForeignKey(Localidad, on_delete=models.PROTECT, related_name="localidad_establecimiento")
    telefono = models.CharField("Número de teléfono", max_length=50)
    email = models.EmailField("E-mail", max_length=100)
    web = models.CharField("Dirección Web", max_length=200)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s' % (self.nombre, self.razon_social, self.direccion,
                                               self.localidad, self.telefono, self.email,
                                               self.web)


class PiezaDental(models.Model):
    nombre = models.CharField("Nombre de la pieza dental", max_length=50, primary_key=True)

    class Meta:
        verbose_name_plural = 'Piezas dentales'

    def __str__(self):
        return self.nombre


class Prestacion(models.Model):
    nombre = models.CharField("Nombre de la prestación", max_length=100, primary_key=True)
    descripcion = models.CharField("Descripción de la prestación", max_length=300)
    pieza_dental = models.ForeignKey(PiezaDental, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Prestaciones'

    def __str__(self):
        return '%s, %s, %s' % (self.nombre, self.descripcion, self.pieza_dental)


class Tratamiento(models.Model):
    medico_efector = models.ForeignKey(Profesional, on_delete=models.PROTECT)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT)
    fecha = models.DateField
    observaciones = models.CharField("Observaciones", max_length=1000)

    def __str__(self):
        return '%s, %s, %s, %s' % (self.medico_efector, self.prestacion, self.fecha, self.observaciones)


class FichaMedica(models.Model):
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, primary_key=True)
    fecha_alta = models.DateField("Fecha de alta")
    tipo_factor_sangre = models.CharField("Tipo y factor de sangre", max_length=3)
    antecedentes = models.CharField(max_length=1000)
    medicacion = models.CharField("Medicación", max_length=1000)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT)
    hc = models.ForeignKey(Tratamiento, on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s, %s, %s' % (self.establecimiento, self.paciente, self.fecha_alta,
                                                   self.tipo_factor_sangre, self.antecedentes, self.medicacion,
                                                   self.prestacion, self.hc)


class FichaMedicaTratamiento(models.Model):
    fichamedica = models.ForeignKey(FichaMedica, on_delete=models.PROTECT, primary_key=True)
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.fichamedica, self.tratamiento)


class CalendarioTurnos(models.Model):
    dia = models.CharField("Día de la semana", max_length=2, choices=DIA_CHOICE, default='Lu')
    hora = models.DateTimeField

    def __str__(self):
        return '%s, %s' % (self.dia, self.hora)


class TratamientoPrestacion(models.Model):
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.PROTECT)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name="prestacion_tratamiento")

    def __str__(self):
        return '%s, %s' % (self.tratamiento, self.prestacion)


class PrestacionPzaDental(models.Model):
    prestacion = models.ForeignKey(Prestacion, on_delete=models.PROTECT, related_name="prestacion_pzadental")
    pieza_dental = models.ForeignKey(PiezaDental, on_delete=models.PROTECT)

    def __str__(self):
        return '%s, %s' % (self.prestacion, self.pieza_dental)
