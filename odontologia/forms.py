from django import forms
from django.forms import ModelForm
from .models import Localidad, \
    Persona, \
    Usuario, \
    Paciente, \
    Profesional, \
    ObraSocial, \
    Turno, \
    Establecimiento, \
    PiezaDental, \
    Prestacion, \
    Tratamiento, \
    FichaMedica, \
    FichaMedicaTratamiento, \
    CalendarioTurnos, \
    TratamientoPrestacion, \
    PrestacionPzaDental


class DateInput(forms.DateInput):
    input_type = 'date'


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime'


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                    'placeholder': 'Nombre'}),
                   'cp': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                     'placeholder': 'Código Postal'}),
                   }
        # si fuesen solo algunos campos, armar una tupla: ("nombre", "num_doc")


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                    'placeholder': 'Nombre/s'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                      'placeholder': 'Apellido'}),
                   'num_doc': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                     'placeholder': 'Número de documento'}),
                   'num_cuit': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                      'placeholder': 'Número de CUIT'}),
                   'fecha_nac': DateInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control input',
                                                      'placeholder': 'Número de teléfono'}),
                   'email': forms.TextInput(attrs={'class': 'form-control input',
                                                   'placeholder': 'Dirección de e-mail'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control input',
                                                       'placeholder': 'Domicilio'}),
                   'localidad': forms.Select(attrs={'class': 'form-control input'})
                   }


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {'persona': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                     'placeholder': 'Persona'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                    'placeholder': 'Nombre de usuario'}),
                   'password': forms.TextInput(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                      'placeholder': 'Contraseña'})
                   }


class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {'paciente': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                   'placeholder': 'Nombre del paciente'}),
                   'num_hc': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                    'placeholder': 'Número de Historia Clínica'}),
                   'num_os': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                    'placeholder': 'Número de Obra Social'}),
                   'titular': forms.CheckboxInput(attrs={'is_checkbox': True})
                   }


class ProfesionalForm(ModelForm):
    class Meta:
        model = Profesional
        fields = '__all__'
        widgets = {'profesional': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize',
                                                   'placeholder': 'Nombre del profesional'}),
                   'matricula': forms.TextInput(attrs={'type': 'number', 'class': 'form-control input',
                                                    'placeholder': 'Número de matrícula'}),
                   'especialidad': forms.TextInput(attrs={'class': 'form-control input',
                                                    'placeholder': 'Especialidad'}),
                   }


class ObraSocialForm(ModelForm):
    class Meta:
        model = ObraSocial
        fields = '__all__'


class TurnoForm(ModelForm):
    class Meta:
        model = Turno
        fields = '__all__'
        widgets = {'paciente': forms.Select(attrs={'class': 'form-control input', 'text-transform': 'capitalize'}),
                   'medico': forms.Select(attrs={'type': 'number', 'class': 'form-control input'}),
                   'turno': forms.DateTimeInput(format='%Y-%m-%d', attrs={'class': 'form-control input-sm'}),
                   'estado': forms.TextInput(attrs={'class': 'form-control input',
                                                    'placeholder': 'Estado del turno'}),
                   }

class EstablecimientoForm(ModelForm):
    class Meta:
        model = Establecimiento
        fields = '__all__'


class PiezaDentalForm(ModelForm):
    class Meta:
        model = PiezaDental
        fields = '__all__'


class PrestacionForm(ModelForm):
    class Meta:
        model = Prestacion
        fields = '__all__'


class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        fields = '__all__'


class FichaMedicaForm(ModelForm):
    class Meta:
        model = FichaMedica
        fields = '__all__'


class FichaMedicaTratamientoForm(ModelForm):
    class Meta:
        model = FichaMedicaTratamiento
        fields = '__all__'


class CalendarioTurnosForm(ModelForm):
    class Meta:
        model = CalendarioTurnos
        fields = '__all__'


class TratamientoPrestacionForm(ModelForm):
    class Meta:
        model = TratamientoPrestacion
        fields = '__all__'


class PrestacionPzaDentalForm(ModelForm):
    class Meta:
        model = PrestacionPzaDental
        fields = '__all__'
