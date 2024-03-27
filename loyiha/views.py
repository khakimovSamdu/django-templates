from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Smartphone
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here

class RegistratsiyaPage(TemplateView):
    template_name = 'register.html'

def get_add(request: HttpRequest):
    if request.method=='POST':
        data = request.body.decode('utf-8')
        data = json.loads(data)
        create = Smartphone.objects.create(
            name = data['name'],
            company = data['company'],
            color = data['color'],
            RAM = data['RAM'],
            memory = data['memory'],
            price = data['price'], 
            img_url = data['img_url'], 
        )
        return JsonResponse({"statust":"OK"})
    else:
        return JsonResponse({"Method":"Error"})