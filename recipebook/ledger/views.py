from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipe_list(request):
    return HttpResponse("template")

#def recipe_with_param(request, param="list"):
    #template for recipe 1 & 2