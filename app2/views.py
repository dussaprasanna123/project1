from django.shortcuts import render
from django.http import HttpResponse     
# create your views here.
def radha(request):
  return HttpResponse('<h1><marquee>my mom is my world</marquee></h1>')