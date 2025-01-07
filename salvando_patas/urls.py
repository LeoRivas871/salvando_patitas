from django.urls import path
from . import views

app_name = 'salvando_patas'
urlpatterns = [
    path('',views.index,name='index'),
]