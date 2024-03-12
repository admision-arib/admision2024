from django import forms
from .models import Postulante


class RegistroPostulanteForm(forms.ModelForm):
    fecha_nacimiento=forms.DateField(label='Fecha de Nacimiento',  widget=forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa'}))

    class Meta:
        model = Postulante
        fields = ['nombres', 'apellido_paterno', 'apellido_materno',
                  'dni', 'correo', 'genero', 'celular', 'fecha_nacimiento',
                  'lugar_nacimiento', 'lugar_nacimiento_distrito',
                  'lugar_nacimiento_provincia', 'lugar_nacimiento_departamento',
                  'tutor_apellidos', 'tutor_nombres','tutor_parentesco',
                  'nombre_ies','tipo_institucion', 'anio_egreso', 'direccion_institucion',
                  'institucion_distrito', 'institucion_provincia', 'institucion_departamento',
                   'programa_postula_primera_opcion','programa_postula_segunda_opcion',
                    'enterado_proceso_admision', 'codigo_voucher', 'imagen1','imagen2', 'imagen3', 'imagen4' ]



