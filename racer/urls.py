from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('racer/', views.racer, name='racer'),
    path('all-racer/', views.allracer, name='all-racer'),
    path('all-zavod/', views.allzavod, name='all-zavod'),
    path('all-racer/details/<int:id>', views.details, name='details'),
    path('all-zavod/zavod/<int:id>', views.details_zavod, name='details_zavod'),
    path('all-zavod/zavod/prihlaska/', views.prihlaska, name='prihlaska'),
    path('private-policy/', views.policy, name='private-policy'),
]