from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('./index.html')

def list(request):
    return render_to_response('./collection_list.html')

def add(request):
    return render_to_response('./collection_add.html')