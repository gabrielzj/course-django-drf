from django.shortcuts import render

from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse('home')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')
