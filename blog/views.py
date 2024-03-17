__author__ = 'Sara Fernandes'

from django.shortcuts import render_to_response, render
from django.template import RequestContext, loader

#from django.http import HttpResponseRedirect # Funcao para redirecionar o usuario
#Criar as Views aqui

# pagina inicial do projeto dweb

def homepage(request):
    return render_to_response('index.html',
        context_instance= RequestContext(request))