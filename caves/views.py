from django.shortcuts import render
from django.views import generic
from .models import Cave

# Create your views here.

class CaveList(generic.ListView):
   queryset = Cave.objects.all()
   template_name = "cave/index.html"
   paginate_by = 100