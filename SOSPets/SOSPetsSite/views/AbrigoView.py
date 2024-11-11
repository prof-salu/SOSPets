from django.shortcuts import render
from SOSPetsSite.models import Abrigo


def lista_abrigos(request):

    abrigos = Abrigo.objects.all

    context = {'abrigos': abrigos}
    return render(request, 'abrigos/lista_abrigos.html', context)

