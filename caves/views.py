from django.shortcuts import render
# Test
from django.http import HttpResponse

# Create your views here.

def my_test(request):
   return HttpResponse("Test")
