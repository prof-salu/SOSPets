from django.urls import path
from SOSPetsSite.views.AbrigoView import lista_abrigos


urlpatterns = [
    path("", lista_abrigos, name='abrigos'),
]