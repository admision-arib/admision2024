from django.urls import path
#from .views import registro_exitoso, listar_postulantes, registrar, postulante_print, 
from . import views
#from .views import ConfirmacionView
from .utils import generar_pdf


"""The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
app_name = 'postulantes'

urlpatterns = [
    path('registrar/', views.registrar, name='registrar_postulante'),
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
    path('listar/', views.listar_postulantes, name='listar_postulantes'),
    path('generar_pdf/ficha/<int:pk>', views.postulante_print, name='generar_pdf' ),
]