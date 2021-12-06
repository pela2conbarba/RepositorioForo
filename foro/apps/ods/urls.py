from django.urls import path
from . import views

app_name = 'ods'

urlpatterns = [
    path('listar/', views.listarods, name = 'listar_ods')
]