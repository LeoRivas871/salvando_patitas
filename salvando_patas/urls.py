from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'salvando_patas'
urlpatterns = [
    path('',views.index,name='index'),
    path('organizacion/',views.organization,name='organizacion'),
    path('team/',views.miembros,name='team'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
