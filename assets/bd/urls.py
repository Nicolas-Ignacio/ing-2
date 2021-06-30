from django.urls import path
from .views import home, poblar_bd, ropa, ropa_tienda, ropa_ficha
 
urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('ropa/<action>/<id>', ropa, name="ropa"),
    path('ropa_tienda', ropa_tienda, name="ropa_tienda"),
    path('ropa_ficha/<id>', ropa_ficha, name="ropa_ficha"),
]