from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('home/',views.login_view),
    path('registrarEcosistema/', views.registrarEcosistema),
    path('edicionEcosistema/<nombre>', views.edicionEcosistema),
    path('editarEcosistema/', views.editarEcosistema),
    path('eliminarEcosistema/<nombre>', views.eliminarEcosistema),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
