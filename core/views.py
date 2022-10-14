import imp
from django.http import HttpResponse
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from core.models import Categoria

import json

def teste(request):
    return HttpResponse('Teste')

def teste2(request):
    
    return HttpResponse('Teste2') 


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request ):
        data = list(Categoria.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type="application/json")
