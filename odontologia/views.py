from django.shortcuts import render, redirect
from .models import Persona, Paciente, Profesional, Localidad, \
    Establecimiento, Usuario, ObraSocial, Turno, PiezaDental, \
    Prestacion, Tratamiento, FichaMedica, FichaMedicaTratamiento,\
    CalendarioTurnos, TratamientoPrestacion, PrestacionPzaDental
from .forms import PersonaForm, PacienteForm, UsuarioForm, ProfesionalForm, LocalidadForm


def index(request, template_name='odontologia/index.html'):
    return render(request, template_name)


def localidades_listar(request, template_name='odontologia/localidades.html'):
    localidades = Localidad.objects.all()
    dato_localidades = {"localidades": localidades}
    return render(request, template_name, dato_localidades)


def personas_listar(request, template_name='odontologia/personas.html'):
    personas = Persona.objects.all()
    dato_personas = {"personas": personas}
    return render(request, template_name, dato_personas)


def pacientes_listar(request, template_name='odontologia/pacientes.html'):
    pacientes = Paciente.objects.all()
    dato_pacientes = {"pacientes": pacientes}
    return render(request, template_name, dato_pacientes)


def profesionales_listar(request, template_name='odontologia/profesionales.html'):
    profesionales = Profesional.objects.all()
    dato_profesionales = {"profesionales": profesionales}
    return render(request, template_name, dato_profesionales)


def establecimientos_listar(request, template_name='odontologia/establecimientos.html'):
    establecimientos = Establecimiento.objects.all()
    dato_establecimientos = {"establecimientos": establecimientos}
    return render(request, template_name, dato_establecimientos)


def usuarios_listar(request, template_name='odontologia/usuarios.html'):
    usuarios = Usuario.objects.all()
    dato_usuarios = {"usuarios": usuarios}
    return render(request, template_name, dato_usuarios)


def obrassociales_listar(request, template_name='odontologia/obras_sociales.html'):
    obra_social = ObraSocial.objects.all()
    dato_obrassociales = {"obras sociales": obra_social}
    return render(request, template_name, dato_obrassociales)


def turnos_listar(request, template_name='odontologia/turnos.html'):
    turnos = Turno.objects.all()
    dato_turnos = {"turnos": turnos}
    return render(request, template_name, dato_turnos)


def pzasdentales_listar(request, template_name='odontologia/piezas_dentales.html'):
    piezas_dentales = PiezaDental.objects.all()
    dato_pzasdentales = {"piezas dentales": piezas_dentales}
    return render(request, template_name, dato_pzasdentales)


def prestaciones_listar(request, template_name='odontologia/prestaciones.html'):
    prestaciones = Prestacion.objects.all()
    dato_prestaciones = {"prestaciones": prestaciones}
    return render(request, template_name, dato_prestaciones)


def tratamientos_listar(request, template_name='odontologia/tratamientos.html'):
    tratamientos = Tratamiento.objects.all()
    dato_tratamientos = {"tratamientos": tratamientos}
    return render(request, template_name, dato_tratamientos)


def fichasmedicas_listar(request, template_name='odontologia/fichas_medicas.html'):
    fichas_medicas = FichaMedica.objects.all()
    dato_fichasmedicas = {"fichas médicas": fichas_medicas}
    return render(request, template_name, dato_fichasmedicas)


def fichamedicatratamiento_listar(request, template_name='odontologia/fichamedicatratamiento.html'):
    fichamedicatratamiento = FichaMedicaTratamiento.objects.all()
    dato_fichamedicatratamiento = {"Ficha Médica - Tratamiento": fichamedicatratamiento}
    return render(request, template_name, dato_fichamedicatratamiento)


def calendarioturnos_listar(request, template_name='odontologia/calendarioturnos.html'):
    calendarioturnos = CalendarioTurnos.objects.all()
    dato_calendarioturnos = {"Calendario - Turnos": calendarioturnos}
    return render(request, template_name, dato_calendarioturnos)


def prestacionpiezadental_listar(request, template_name='odontologia/prestacionpiezadental.html'):
    prestacionpiezadental = PrestacionPzaDental.objects.all()
    dato_prestacionpzadental = {"Prestación - Pieza dental": prestacionpiezadental}
    return render(request, template_name, dato_prestacionpzadental)


def tratamientoprestacion_listar(request, template_name='odontologia/tratamientoprestacion.html'):
    tratamientoprestacion = TratamientoPrestacion.objects.all()
    dato_tratamientoprestacion = {"Tratamiento - Prestación": tratamientoprestacion}
    return render(request, template_name, dato_tratamientoprestacion)


def nueva_localidad(request, template_name='odontologia/localidad_form.html'):
    if request.method == 'POST':
        form = LocalidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('localidades')
    else:
        form = LocalidadForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nueva_persona(request, template_name='odontologia/persona_form.html'):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('personas')
    else:
        form = PersonaForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nuevo_paciente(request, template_name='odontologia/paciente_form.html'):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('pacientes')
    else:
        form = PacienteForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nuevo_usuario(request, template_name='odontologia/usuario_form.html'):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def nuevo_profesional(request, template_name='odontologia/profesional_form.html'):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profesionales')
    else:
        form = ProfesionalForm()
    dato = {"form": form}
    return render(request, template_name, dato)


def modificar_persona(request, pk, template_name='odontologia/persona_form.html'):
    persona = Persona.objects.get(num_doc=pk)
    form = PersonaForm(request.POST or None, instance=persona)
    if form.is_valid():
        form.save(commit=True)
        return redirect('personas')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def modificar_profesional(request, pk, template_name='odontologia/profesional_form.html'):
    profesional = Profesional.objects.get(matricula=pk)
    form = ProfesionalForm(request.POST or None, instance=profesional)
    if form.is_valid():
        form.save(commit=True)
        return redirect('profesionales')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def modificar_paciente(request, pk, template_name='odontologia/paciente_form.html'):
    paciente = Paciente.objects.get(num_hc=pk)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save(commit=True)
        return redirect('pacientes')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def modificar_usuario(request, pk, template_name='odontologia/usuario_form.html'):
    usuario = Usuario.objects.get(nombre=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save(commit=True)
        return redirect('usuarios')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def modificar_localidad(request, pk, template_name='odontologia/localidad_form.html'):
    localidad = Localidad.objects.get(cp=pk)
    form = LocalidadForm(request.POST or None, instance=localidad)
    if form.is_valid():
        form.save(commit=True)
        return redirect('localidades')
    else:
        print(form.errors)
    datos = {'form': form}
    return render(request, template_name, datos)


def eliminar_persona(request, pk, template_name='odontologia/persona_conf_elim.html'):
    persona = Persona.objects.get(num_doc=pk)
    if request.method == 'POST':
        persona.delete()
        return redirect('personas')
    else:
        return render(request, template_name, {'form': persona})


def eliminar_profesional(request, pk, template_name='odontologia/profesional_conf_elim.html'):
    profesional = Profesional.objects.get(matricula=pk)
    if request.method == 'POST':
        profesional.delete()
        return redirect('profesionales')
    else:
        return render(request, template_name, {'form': profesional})


def eliminar_paciente(request, pk, template_name='odontologia/paciente_conf_elim.html'):
    paciente = Paciente.objects.get(num_hc=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('pacientes')
    else:
        return render(request, template_name, {'form': paciente})


def eliminar_usuario(request, pk, template_name='odontologia/usuario_conf_elim.html'):
    usuario = Usuario.objects.get(nombre=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    else:
        return render(request, template_name, {'form': usuario})


def eliminar_localidad(request, pk, template_name='odontologia/localidad_conf_elim.html'):
    localidad = Localidad.objects.get(cp=pk)
    if request.method == 'POST':
        localidad.delete()
        return redirect('localidades')
    else:
        return render(request, template_name, {'form': localidad})
