from . import views 
from django.urls import path, include
from django.contrib import admin



urlpatterns = [
    path('', views.telainicial, name='telainicial'),
    path('editarperfil', views.editarperfil, name='editarperfil'),
    path('func/new', views.newfunc, name='novofunc'),
    path('func/list', views.listafunc, name='listafunc'),
    path('func/<int:pk>/edit/', views.editfunc, name='editfunc'),
    path('func/<int:pk>/delete/', views.deletefunc, name='deletefunc'),
    path('ponto/new', views.pontonew, name='novoponto'),
    path('relatoriogeral', views.relatoriogeral, name='relatoriogeral'),
    path('relatorioespecifico/<int:pk>', views.relatorioespecifico, name='relatorioespecifico'),
    path('func/<int:pk>/more', views.morefunc, name='morefunc'),
    path('cargo/new', views.newcargo, name='novocargo'),
    path('cargo/list', views.listacargo, name='listacargo'),
    path('cargo/<int:pk>/edit/', views.editcargo, name='editcargo'),
    path('cargo/<int:pk>/delete/', views.deletecargo, name='deletecargo'),

    path('contato/', views.contato, name='contato'),
    path('contato/obg', views.obg, name='obg'),
]