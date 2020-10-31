from django.contrib import admin
from django.urls import path,include
from .views import index,galeria,ingresar,insumos,quienes,registro,ubicacion,logout_sesion,admin_insumos, eliminar, modificar_vista, modificar

urlpatterns = [
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALE'),
    path('ingresar/',ingresar,name='INGRE'),
    path('insumos/',insumos,name='INSU'),
    path('quienesomos/',quienes,name='QUIEN'),
    path('registro/',registro,name='REG'),
    path('ubicacion/',ubicacion,name='UBI'),
    path('logout_sesion/',logout_sesion,name='LOGOUT'),
    path('adm_insumos/',admin_insumos,name='ADM_IN'),
    path('eliminar/<id>/',eliminar,name='ELIMINAR'),
    path('modificar_vista/<id>/',modificar_vista,name='MODIFICAR_V'),
    path('modificar/',modificar,name='MODIFICAR'),
]
