from django.shortcuts import render

# Create your views here.
from logging import info
from re import S
from django.shortcuts import render

import json
import requests
# Create your views here.
def nep(request):
  
    result=requests.get('https://restcountries.com/v2/all').json
           
    
    return render(request, "countrydatas/index.html",{'result':result})