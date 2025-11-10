from django.urls import path
from inicio.views import principal,paradas, crear_maquina, listado_maquinas
urlpatterns = [ 
    path('', principal),
    path('paradas/', paradas),
    #path('crear-maquina/', crear_maquina),
    path('crear-maquina/<marca>/<proceso>/<descripcion>/', crear_maquina),
    path('listado-maquinas/', listado_maquinas)
    

]