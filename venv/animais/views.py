from django.shortcuts import render
from animais.models import Animais

"""def lista_animais(request):
    query = request.GET.get('pesquisa')
    
    if query:
        animais = Animais.objects.filter(nome__icontains=query)
    else:
        animais = Animais.objects.all()

    return render(request, 'lista_animais.html', {'animais': animais})"""

